# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Warehouse'
        db.create_table(u'stocks_warehouse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('location', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'stocks', ['Warehouse'])

        # Adding model 'Product'
        db.create_table(u'stocks_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('retail_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('lowest_retail_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('wholesale_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('lowest_wholesale_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
        ))
        db.send_create_signal(u'stocks', ['Product'])

        # Adding model 'Item'
        db.create_table(u'stocks_item', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['stocks.Product'], unique=True, primary_key=True)),
            ('cost_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal(u'stocks', ['Item'])

        # Adding model 'ItemQuantity'
        db.create_table(u'stocks_itemquantity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Item'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'stocks', ['ItemQuantity'])

        # Adding model 'Package'
        db.create_table(u'stocks_package', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['stocks.Product'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'stocks', ['Package'])

        # Adding model 'PackageItem'
        db.create_table(u'stocks_packageitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Package'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Item'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'stocks', ['PackageItem'])

        # Adding unique constraint on 'PackageItem', fields ['package', 'item']
        db.create_unique(u'stocks_packageitem', ['package_id', 'item_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'PackageItem', fields ['package', 'item']
        db.delete_unique(u'stocks_packageitem', ['package_id', 'item_id'])

        # Deleting model 'Warehouse'
        db.delete_table(u'stocks_warehouse')

        # Deleting model 'Product'
        db.delete_table(u'stocks_product')

        # Deleting model 'Item'
        db.delete_table(u'stocks_item')

        # Deleting model 'ItemQuantity'
        db.delete_table(u'stocks_itemquantity')

        # Deleting model 'Package'
        db.delete_table(u'stocks_package')

        # Deleting model 'PackageItem'
        db.delete_table(u'stocks_packageitem')


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
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lowest_retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'lowest_wholesale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
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