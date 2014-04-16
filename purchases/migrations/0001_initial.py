# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Supplier'
        db.create_table('purchases_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True)),
            ('partner', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partners.Partner'], unique=True)),
        ))
        db.send_create_signal('purchases', ['Supplier'])

        # Adding model 'PurchaseOrder'
        db.create_table('purchases_purchaseorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Supplier'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('purchases', ['PurchaseOrder'])

        # Adding unique constraint on 'PurchaseOrder', fields ['serial_number', 'supplier']
        db.create_unique('purchases_purchaseorder', ['serial_number', 'supplier_id'])

        # Adding model 'PurchaseOrderLine'
        db.create_table('purchases_purchaseorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purchase_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.PurchaseOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal('purchases', ['PurchaseOrderLine'])

        # Adding model 'Invoice'
        db.create_table('purchases_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Supplier'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('payment_due_date', self.gf('django.db.models.fields.DateField')()),
            ('payment_made_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
        ))
        db.send_create_signal('purchases', ['Invoice'])

        # Adding unique constraint on 'Invoice', fields ['serial_number', 'supplier']
        db.create_unique('purchases_invoice', ['serial_number', 'supplier_id'])

        # Adding model 'InvoiceLine'
        db.create_table('purchases_invoiceline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Invoice'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal('purchases', ['InvoiceLine'])

        # Adding model 'DeliveryOrder'
        db.create_table('purchases_deliveryorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Supplier'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('good_received_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
        ))
        db.send_create_signal('purchases', ['DeliveryOrder'])

        # Adding unique constraint on 'DeliveryOrder', fields ['serial_number', 'supplier']
        db.create_unique('purchases_deliveryorder', ['serial_number', 'supplier_id'])

        # Adding model 'DeliveryOrderLine'
        db.create_table('purchases_deliveryorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('delivery_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.DeliveryOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('purchases', ['DeliveryOrderLine'])


    def backwards(self, orm):
        # Removing unique constraint on 'DeliveryOrder', fields ['serial_number', 'supplier']
        db.delete_unique('purchases_deliveryorder', ['serial_number', 'supplier_id'])

        # Removing unique constraint on 'Invoice', fields ['serial_number', 'supplier']
        db.delete_unique('purchases_invoice', ['serial_number', 'supplier_id'])

        # Removing unique constraint on 'PurchaseOrder', fields ['serial_number', 'supplier']
        db.delete_unique('purchases_purchaseorder', ['serial_number', 'supplier_id'])

        # Deleting model 'Supplier'
        db.delete_table('purchases_supplier')

        # Deleting model 'PurchaseOrder'
        db.delete_table('purchases_purchaseorder')

        # Deleting model 'PurchaseOrderLine'
        db.delete_table('purchases_purchaseorderline')

        # Deleting model 'Invoice'
        db.delete_table('purchases_invoice')

        # Deleting model 'InvoiceLine'
        db.delete_table('purchases_invoiceline')

        # Deleting model 'DeliveryOrder'
        db.delete_table('purchases_deliveryorder')

        # Deleting model 'DeliveryOrderLine'
        db.delete_table('purchases_deliveryorderline')


    models = {
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '15'})
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
        'purchases.deliveryorder': {
            'Meta': {'object_name': 'DeliveryOrder', 'unique_together': "(['serial_number', 'supplier'],)"},
            'good_received_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.Supplier']"})
        },
        'purchases.deliveryorderline': {
            'Meta': {'object_name': 'DeliveryOrderLine'},
            'delivery_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.DeliveryOrder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'purchases.invoice': {
            'Meta': {'object_name': 'Invoice', 'unique_together': "(['serial_number', 'supplier'],)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'payment_due_date': ('django.db.models.fields.DateField', [], {}),
            'payment_made_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.Supplier']"})
        },
        'purchases.invoiceline': {
            'Meta': {'object_name': 'InvoiceLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.Invoice']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'purchases.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder', 'unique_together': "(['serial_number', 'supplier'],)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.Supplier']"})
        },
        'purchases.purchaseorderline': {
            'Meta': {'object_name': 'PurchaseOrderLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'purchase_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.PurchaseOrder']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'})
        },
        'purchases.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['partners.Partner']", 'unique': 'True'})
        }
    }

    complete_apps = ['purchases']