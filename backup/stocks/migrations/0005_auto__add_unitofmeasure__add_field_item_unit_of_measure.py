# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UnitOfMeasure'
        db.create_table(u'stocks_unitofmeasure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'stocks', ['UnitOfMeasure'])

        # Adding field 'Item.unit_of_measure'
        db.add_column(u'stocks_item', 'unit_of_measure',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['stocks.UnitOfMeasure']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'UnitOfMeasure'
        db.delete_table(u'stocks_unitofmeasure')

        # Deleting field 'Item.unit_of_measure'
        db.delete_column(u'stocks_item', 'unit_of_measure_id')


    models = {
        u'stocks.item': {
            'Meta': {'object_name': 'Item', '_ormbases': [u'stocks.Product']},
            'cost_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['stocks.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'unit_of_measure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.UnitOfMeasure']"})
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