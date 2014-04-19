# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Salesperson'
        db.create_table('wholesales_salesperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('wholesales', ['Salesperson'])

        # Adding model 'SalesTerm'
        db.create_table('wholesales_salesterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('wholesales', ['SalesTerm'])

        # Adding model 'Customer'
        db.create_table('wholesales_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['partners.Partner'])),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.Salesperson'])),
            ('sales_term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.SalesTerm'])),
        ))
        db.send_create_signal('wholesales', ['Customer'])

        # Adding model 'SalesOrder'
        db.create_table('wholesales_salesorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.Customer'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('sales_term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.SalesTerm'])),
        ))
        db.send_create_signal('wholesales', ['SalesOrder'])

        # Adding model 'SalesOrderLine'
        db.create_table('wholesales_salesorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sales_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.SalesOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal('wholesales', ['SalesOrderLine'])

        # Adding model 'SalesDeliveryOrder'
        db.create_table('wholesales_salesdeliveryorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.Customer'])),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('good_sent_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('wholesales', ['SalesDeliveryOrder'])

        # Adding model 'SalesDeliveryOrderLine'
        db.create_table('wholesales_salesdeliveryorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('delivery_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.SalesDeliveryOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('wholesales', ['SalesDeliveryOrderLine'])


    def backwards(self, orm):
        # Deleting model 'Salesperson'
        db.delete_table('wholesales_salesperson')

        # Deleting model 'SalesTerm'
        db.delete_table('wholesales_salesterm')

        # Deleting model 'Customer'
        db.delete_table('wholesales_customer')

        # Deleting model 'SalesOrder'
        db.delete_table('wholesales_salesorder')

        # Deleting model 'SalesOrderLine'
        db.delete_table('wholesales_salesorderline')

        # Deleting model 'SalesDeliveryOrder'
        db.delete_table('wholesales_salesdeliveryorder')

        # Deleting model 'SalesDeliveryOrderLine'
        db.delete_table('wholesales_salesdeliveryorderline')


    models = {
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'telephone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'})
        },
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
        'wholesales.customer': {
            'Meta': {'object_name': 'Customer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['partners.Partner']"}),
            'sales_term': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.SalesTerm']"}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.Salesperson']"})
        },
        'wholesales.salesdeliveryorder': {
            'Meta': {'object_name': 'SalesDeliveryOrder'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.Customer']"}),
            'good_sent_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {})
        },
        'wholesales.salesdeliveryorderline': {
            'Meta': {'object_name': 'SalesDeliveryOrderLine'},
            'delivery_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.SalesDeliveryOrder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'wholesales.salesorder': {
            'Meta': {'object_name': 'SalesOrder'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'sales_term': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.SalesTerm']"})
        },
        'wholesales.salesorderline': {
            'Meta': {'object_name': 'SalesOrderLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.SalesOrder']"}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'})
        },
        'wholesales.salesperson': {
            'Meta': {'object_name': 'Salesperson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'wholesales.salesterm': {
            'Meta': {'object_name': 'SalesTerm'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['wholesales']