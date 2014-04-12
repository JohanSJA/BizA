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
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('stocks', ['Uom'])

        # Adding model 'Stock'
        db.create_table('stocks_stock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['products.Product'])),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Uom'])),
        ))
        db.send_create_signal('stocks', ['Stock'])

        # Adding model 'Warehouse'
        db.create_table('stocks_warehouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('stocks', ['Warehouse'])

        # Adding model 'Log'
        db.create_table('stocks_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Stock'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
        ))
        db.send_create_signal('stocks', ['Log'])

        # Adding unique constraint on 'Log', fields ['stock', 'warehouse']
        db.create_unique('stocks_log', ['stock_id', 'warehouse_id'])

        # Adding model 'LogEntry'
        db.create_table('stocks_logentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Log'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('stocks', ['LogEntry'])


    def backwards(self, orm):
        # Removing unique constraint on 'Log', fields ['stock', 'warehouse']
        db.delete_unique('stocks_log', ['stock_id', 'warehouse_id'])

        # Deleting model 'Uom'
        db.delete_table('stocks_uom')

        # Deleting model 'Stock'
        db.delete_table('stocks_stock')

        # Deleting model 'Warehouse'
        db.delete_table('stocks_warehouse')

        # Deleting model 'Log'
        db.delete_table('stocks_log')

        # Deleting model 'LogEntry'
        db.delete_table('stocks_logentry')


    models = {
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'stocks.log': {
            'Meta': {'unique_together': "(['stock', 'warehouse'],)", 'object_name': 'Log'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Stock']"}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'stocks.logentry': {
            'Meta': {'object_name': 'LogEntry'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Log']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['products.Product']"}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Uom']"})
        },
        'stocks.uom': {
            'Meta': {'object_name': 'Uom'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['stocks']