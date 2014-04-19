# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table('retails_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
        ))
        db.send_create_signal('retails', ['Store'])

        # Adding model 'Salesperson'
        db.create_table('retails_salesperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Store'])),
            ('register_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('retails', ['Salesperson'])

        # Adding model 'RetailSales'
        db.create_table('retails_retailsales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Store'])),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Salesperson'])),
            ('serial_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, blank=True, null=True)),
            ('closed_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
        ))
        db.send_create_signal('retails', ['RetailSales'])

        # Adding model 'RetailSalesLine'
        db.create_table('retails_retailsalesline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('retail_sales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.RetailSales'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=12)),
        ))
        db.send_create_signal('retails', ['RetailSalesLine'])


    def backwards(self, orm):
        # Deleting model 'Store'
        db.delete_table('retails_store')

        # Deleting model 'Salesperson'
        db.delete_table('retails_salesperson')

        # Deleting model 'RetailSales'
        db.delete_table('retails_retailsales')

        # Deleting model 'RetailSalesLine'
        db.delete_table('retails_retailsalesline')


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
        'retails.retailsales': {
            'Meta': {'object_name': 'RetailSales'},
            'closed_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['retails.Salesperson']"}),
            'serial_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['retails.Store']"})
        },
        'retails.retailsalesline': {
            'Meta': {'object_name': 'RetailSalesLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'retail_sales': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['retails.RetailSales']"}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'})
        },
        'retails.salesperson': {
            'Meta': {'object_name': 'Salesperson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'register_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['retails.Store']"})
        },
        'retails.store': {
            'Meta': {'object_name': 'Store'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['retails']