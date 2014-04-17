# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('wholesales_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True)),
            ('partner', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['partners.Partner'])),
        ))
        db.send_create_signal('wholesales', ['Customer'])

        # Adding model 'SalesOrder'
        db.create_table('wholesales_salesorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.Customer'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('wholesales', ['SalesOrder'])

        # Adding model 'SalesOrderLine'
        db.create_table('wholesales_salesorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sales_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.SalesOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=12)),
        ))
        db.send_create_signal('wholesales', ['SalesOrderLine'])

        # Adding model 'SalesInvoice'
        db.create_table('wholesales_salesinvoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.Customer'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('payment_due_date', self.gf('django.db.models.fields.DateField')()),
            ('payment_received_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('wholesales', ['SalesInvoice'])

        # Adding model 'SalesInvoiceLine'
        db.create_table('wholesales_salesinvoiceline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.SalesInvoice'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=12)),
        ))
        db.send_create_signal('wholesales', ['SalesInvoiceLine'])

        # Adding model 'SalesDeliveryOrder'
        db.create_table('wholesales_salesdeliveryorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.Customer'])),
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
        # Deleting model 'Customer'
        db.delete_table('wholesales_customer')

        # Deleting model 'SalesOrder'
        db.delete_table('wholesales_salesorder')

        # Deleting model 'SalesOrderLine'
        db.delete_table('wholesales_salesorderline')

        # Deleting model 'SalesInvoice'
        db.delete_table('wholesales_salesinvoice')

        # Deleting model 'SalesInvoiceLine'
        db.delete_table('wholesales_salesinvoiceline')

        # Deleting model 'SalesDeliveryOrder'
        db.delete_table('wholesales_salesdeliveryorder')

        # Deleting model 'SalesDeliveryOrderLine'
        db.delete_table('wholesales_salesdeliveryorderline')


    models = {
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '12', 'unique': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'wholesales.customer': {
            'Meta': {'object_name': 'Customer'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['partners.Partner']"})
        },
        'wholesales.salesdeliveryorder': {
            'Meta': {'object_name': 'SalesDeliveryOrder'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.Customer']"}),
            'good_sent_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'})
        },
        'wholesales.salesdeliveryorderline': {
            'Meta': {'object_name': 'SalesDeliveryOrderLine'},
            'delivery_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.SalesDeliveryOrder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'wholesales.salesinvoice': {
            'Meta': {'object_name': 'SalesInvoice'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'payment_due_date': ('django.db.models.fields.DateField', [], {}),
            'payment_received_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'})
        },
        'wholesales.salesinvoiceline': {
            'Meta': {'object_name': 'SalesInvoiceLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.SalesInvoice']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'wholesales.salesorder': {
            'Meta': {'object_name': 'SalesOrder'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'})
        },
        'wholesales.salesorderline': {
            'Meta': {'object_name': 'SalesOrderLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sales_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.SalesOrder']"}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'})
        }
    }

    complete_apps = ['wholesales']