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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('purchases', ['Supplier'])

        # Adding model 'PurchaseOrder'
        db.create_table('purchases_purchaseorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Supplier'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('purchases', ['PurchaseOrder'])

        # Adding model 'PurchaseOrderLine'
        db.create_table('purchases_purchaseorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purchase_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.PurchaseOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal('purchases', ['PurchaseOrderLine'])

        # Adding model 'PurchaseDeliveryOrder'
        db.create_table('purchases_purchasedeliveryorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.Supplier'])),
            ('issuing_date', self.gf('django.db.models.fields.DateField')()),
            ('good_received_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('purchases', ['PurchaseDeliveryOrder'])

        # Adding model 'PurchaseDeliveryOrderLine'
        db.create_table('purchases_purchasedeliveryorderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('delivery_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchases.PurchaseDeliveryOrder'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('purchases', ['PurchaseDeliveryOrderLine'])


    def backwards(self, orm):
        # Deleting model 'Supplier'
        db.delete_table('purchases_supplier')

        # Deleting model 'PurchaseOrder'
        db.delete_table('purchases_purchaseorder')

        # Deleting model 'PurchaseOrderLine'
        db.delete_table('purchases_purchaseorderline')

        # Deleting model 'PurchaseDeliveryOrder'
        db.delete_table('purchases_purchasedeliveryorder')

        # Deleting model 'PurchaseDeliveryOrderLine'
        db.delete_table('purchases_purchasedeliveryorderline')


    models = {
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Uom']"})
        },
        'products.uom': {
            'Meta': {'object_name': 'Uom'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'purchases.purchasedeliveryorder': {
            'Meta': {'object_name': 'PurchaseDeliveryOrder'},
            'good_received_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.Supplier']"})
        },
        'purchases.purchasedeliveryorderline': {
            'Meta': {'object_name': 'PurchaseDeliveryOrderLine'},
            'delivery_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['purchases.PurchaseDeliveryOrder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'purchases.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuing_date': ('django.db.models.fields.DateField', [], {}),
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['purchases']