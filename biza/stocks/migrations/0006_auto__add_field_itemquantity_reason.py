# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ItemQuantity.reason'
        db.add_column(u'stocks_itemquantity', 'reason',
                      self.gf('django.db.models.fields.CharField')(default='T', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ItemQuantity.reason'
        db.delete_column(u'stocks_itemquantity', 'reason')


    models = {
        u'stocks.item': {
            'Meta': {'object_name': 'Item', '_ormbases': [u'stocks.Product']},
            'cost_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['stocks.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'unit_of_measure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.UnitOfMeasure']"})
        },
        u'stocks.itemquantity': {
            'Meta': {'ordering': "['-datetime']", 'object_name': 'ItemQuantity'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Item']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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
            'model': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'wholesale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'})
        },
        u'stocks.unitofmeasure': {
            'Meta': {'object_name': 'UnitOfMeasure'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['stocks']