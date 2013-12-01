# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Product', fields ['name']
        db.delete_unique(u'stocks_product', ['name'])

        # Adding field 'Product.model'
        db.add_column(u'stocks_product', 'model',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=12),
                      keep_default=False)


        # Changing field 'Product.name'
        db.alter_column(u'stocks_product', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Product.model'
        db.delete_column(u'stocks_product', 'model')


        # Changing field 'Product.name'
        db.alter_column(u'stocks_product', 'name', self.gf('django.db.models.fields.CharField')(max_length=32, unique=True))
        # Adding unique constraint on 'Product', fields ['name']
        db.create_unique(u'stocks_product', ['name'])


    models = {
        u'stocks.item': {
            'Meta': {'object_name': 'Item', '_ormbases': [u'stocks.Product']},
            'cost_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['stocks.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'stocks.itemquantity': {
            'Meta': {'object_name': 'ItemQuantity'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Item']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Warehouse']"})
        },
        u'stocks.package': {
            'Meta': {'object_name': 'Package', '_ormbases': [u'stocks.Product']},
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['stocks.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'stocks.packageitem': {
            'Meta': {'unique_together': "(['package', 'item'],)", 'object_name': 'PackageItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Item']"}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Package']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'stocks.product': {
            'Meta': {'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lowest_retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'lowest_wholesale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'wholesale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'})
        },
        u'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['stocks']