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
            ('partner', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['partners.Partner'])),
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
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=12)),
        ))
        db.send_create_signal('purchases', ['PurchaseOrderLine'])

        # Adding model 'PurchaseInvoice'
        db.create_table('purchases_purchaseinvoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Supplier'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('payment_due_date', self.gf('django.db.models.fields.DateField')()),
            ('payment_made_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('purchases', ['PurchaseInvoice'])

        # Adding unique constraint on 'PurchaseInvoice', fields ['serial_number', 'supplier']
        db.create_unique('purchases_purchaseinvoice', ['serial_number', 'supplier_id'])

        # Adding model 'PurchaseInvoiceLine'
        db.create_table('purchases_purchaseinvoiceline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.PurchaseInvoice'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=12)),
        ))
        db.send_create_signal('purchases', ['PurchaseInvoiceLine'])

        # Adding model 'PurchaseDeliveryOrder'
        db.create_table('purchases_purchasedeliveryorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Supplier'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('good_received_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('purchases', ['PurchaseDeliveryOrder'])

        # Adding unique constraint on 'PurchaseDeliveryOrder', fields ['serial_number', 'supplier']
        db.create_unique('purchases_purchasedeliveryorder', ['serial_number', 'supplier_id'])

        # Adding model 'PurchaseDeliveryOrderLine'
        db.create_table('purchases_purchasedeliveryorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('delivery_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.PurchaseDeliveryOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('purchases', ['PurchaseDeliveryOrderLine'])


    def backwards(self, orm):
        # Removing unique constraint on 'PurchaseDeliveryOrder', fields ['serial_number', 'supplier']
        db.delete_unique('purchases_purchasedeliveryorder', ['serial_number', 'supplier_id'])

        # Removing unique constraint on 'PurchaseInvoice', fields ['serial_number', 'supplier']
        db.delete_unique('purchases_purchaseinvoice', ['serial_number', 'supplier_id'])

        # Removing unique constraint on 'PurchaseOrder', fields ['serial_number', 'supplier']
        db.delete_unique('purchases_purchaseorder', ['serial_number', 'supplier_id'])

        # Deleting model 'Supplier'
        db.delete_table('purchases_supplier')

        # Deleting model 'PurchaseOrder'
        db.delete_table('purchases_purchaseorder')

        # Deleting model 'PurchaseOrderLine'
        db.delete_table('purchases_purchaseorderline')

        # Deleting model 'PurchaseInvoice'
        db.delete_table('purchases_purchaseinvoice')

        # Deleting model 'PurchaseInvoiceLine'
        db.delete_table('purchases_purchaseinvoiceline')

        # Deleting model 'PurchaseDeliveryOrder'
        db.delete_table('purchases_purchasedeliveryorder')

        # Deleting model 'PurchaseDeliveryOrderLine'
        db.delete_table('purchases_purchasedeliveryorderline')


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
        'purchases.purchasedeliveryorder': {
            'Meta': {'unique_together': "(['serial_number', 'supplier'],)", 'object_name': 'PurchaseDeliveryOrder'},
            'good_received_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.Supplier']"})
        },
        'purchases.purchasedeliveryorderline': {
            'Meta': {'object_name': 'PurchaseDeliveryOrderLine'},
            'delivery_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.PurchaseDeliveryOrder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'purchases.purchaseinvoice': {
            'Meta': {'unique_together': "(['serial_number', 'supplier'],)", 'object_name': 'PurchaseInvoice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'payment_due_date': ('django.db.models.fields.DateField', [], {}),
            'payment_made_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.Supplier']"})
        },
        'purchases.purchaseinvoiceline': {
            'Meta': {'object_name': 'PurchaseInvoiceLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.PurchaseInvoice']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'purchases.purchaseorder': {
            'Meta': {'unique_together': "(['serial_number', 'supplier'],)", 'object_name': 'PurchaseOrder'},
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
            'unit_price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'})
        },
        'purchases.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['partners.Partner']"})
        }
    }

    complete_apps = ['purchases']