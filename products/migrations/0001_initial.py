# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('products_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('products', ['Category'])

        # Adding model 'Uom'
        db.create_table('products_uom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('products', ['Uom'])

        # Adding model 'Product'
        db.create_table('products_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Uom'])),
            ('remark', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('products', ['Product'])

        # Adding model 'Warehouse'
        db.create_table('products_warehouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('products', ['Warehouse'])

        # Adding model 'Log'
        db.create_table('products_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Warehouse'])),
        ))
        db.send_create_signal('products', ['Log'])

        # Adding unique constraint on 'Log', fields ['product', 'warehouse']
        db.create_unique('products_log', ['product_id', 'warehouse_id'])

        # Adding model 'LogEntry'
        db.create_table('products_logentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Log'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['LogEntry'])


    def backwards(self, orm):
        # Removing unique constraint on 'Log', fields ['product', 'warehouse']
        db.delete_unique('products_log', ['product_id', 'warehouse_id'])

        # Deleting model 'Category'
        db.delete_table('products_category')

        # Deleting model 'Uom'
        db.delete_table('products_uom')

        # Deleting model 'Product'
        db.delete_table('products_product')

        # Deleting model 'Warehouse'
        db.delete_table('products_warehouse')

        # Deleting model 'Log'
        db.delete_table('products_log')

        # Deleting model 'LogEntry'
        db.delete_table('products_logentry')


    models = {
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'products.log': {
            'Meta': {'unique_together': "(['product', 'warehouse'],)", 'object_name': 'Log'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Warehouse']"})
        },
        'products.logentry': {
            'Meta': {'object_name': 'LogEntry'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Log']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Uom']"})
        },
        'products.uom': {
            'Meta': {'object_name': 'Uom'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'products.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['products']