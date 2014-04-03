# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Uom'
        db.create_table('stocks_uom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True, unique=True)),
        ))
        db.send_create_signal('stocks', ['Uom'])

        # Adding model 'Category'
        db.create_table('stocks_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
        ))
        db.send_create_signal('stocks', ['Category'])

        # Adding model 'Product'
        db.create_table('stocks_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Uom'])),
            ('barcode', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, unique=True, null=True)),
            ('cost_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4, blank=True, null=True)),
            ('wholesales_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4, blank=True, null=True)),
            ('retail_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4, blank=True, null=True)),
        ))
        db.send_create_signal('stocks', ['Product'])

        # Adding model 'Warehouse'
        db.create_table('stocks_warehouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('address', self.gf('django.db.models.fields.TextField')(unique=True)),
        ))
        db.send_create_signal('stocks', ['Warehouse'])

        # Adding model 'Log'
        db.create_table('stocks_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Product'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
        ))
        db.send_create_signal('stocks', ['Log'])

        # Adding unique constraint on 'Log', fields ['product', 'warehouse']
        db.create_unique('stocks_log', ['product_id', 'warehouse_id'])

        # Adding model 'LogEntry'
        db.create_table('stocks_logentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Log'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('stocks', ['LogEntry'])


    def backwards(self, orm):
        # Removing unique constraint on 'Log', fields ['product', 'warehouse']
        db.delete_unique('stocks_log', ['product_id', 'warehouse_id'])

        # Deleting model 'Uom'
        db.delete_table('stocks_uom')

        # Deleting model 'Category'
        db.delete_table('stocks_category')

        # Deleting model 'Product'
        db.delete_table('stocks_product')

        # Deleting model 'Warehouse'
        db.delete_table('stocks_warehouse')

        # Deleting model 'Log'
        db.delete_table('stocks_log')

        # Deleting model 'LogEntry'
        db.delete_table('stocks_logentry')


    models = {
        'stocks.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'stocks.log': {
            'Meta': {'ordering': "['product', 'warehouse']", 'unique_together': "(['product', 'warehouse'],)", 'object_name': 'Log'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Product']"}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'stocks.logentry': {
            'Meta': {'object_name': 'LogEntry'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Log']"})
        },
        'stocks.product': {
            'Meta': {'ordering': "['code']", 'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'unique': 'True', 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Category']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'cost_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4', 'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4', 'blank': 'True', 'null': 'True'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Uom']"}),
            'wholesales_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4', 'blank': 'True', 'null': 'True'})
        },
        'stocks.uom': {
            'Meta': {'ordering': "['name']", 'object_name': 'Uom'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'stocks.warehouse': {
            'Meta': {'ordering': "['name']", 'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        }
    }

    complete_apps = ['stocks']