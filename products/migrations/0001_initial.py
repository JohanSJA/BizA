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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
        ))
        db.send_create_signal('products', ['Category'])

        # Adding model 'Uom'
        db.create_table('products_uom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('products', ['Uom'])

        # Adding model 'Product'
        db.create_table('products_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('remark', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('products', ['Product'])

        # Adding model 'Pricelist'
        db.create_table('products_pricelist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('base', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['products.Pricelist'], blank=True)),
            ('base_derivation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('products', ['Pricelist'])

        # Adding model 'PricelistEntry'
        db.create_table('products_pricelistentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pricelist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Pricelist'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=12)),
        ))
        db.send_create_signal('products', ['PricelistEntry'])

        # Adding unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.create_unique('products_pricelistentry', ['pricelist_id', 'product_id'])

        # Adding model 'Warehouse'
        db.create_table('products_warehouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('products', ['Warehouse'])

        # Adding model 'BalanceLog'
        db.create_table('products_balancelog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Warehouse'])),
        ))
        db.send_create_signal('products', ['BalanceLog'])

        # Adding unique constraint on 'BalanceLog', fields ['product', 'warehouse']
        db.create_unique('products_balancelog', ['product_id', 'warehouse_id'])

        # Adding model 'BalanceLogEntry'
        db.create_table('products_balancelogentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('balance_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.BalanceLog'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['BalanceLogEntry'])


    def backwards(self, orm):
        # Removing unique constraint on 'BalanceLog', fields ['product', 'warehouse']
        db.delete_unique('products_balancelog', ['product_id', 'warehouse_id'])

        # Removing unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.delete_unique('products_pricelistentry', ['pricelist_id', 'product_id'])

        # Deleting model 'Category'
        db.delete_table('products_category')

        # Deleting model 'Uom'
        db.delete_table('products_uom')

        # Deleting model 'Product'
        db.delete_table('products_product')

        # Deleting model 'Pricelist'
        db.delete_table('products_pricelist')

        # Deleting model 'PricelistEntry'
        db.delete_table('products_pricelistentry')

        # Deleting model 'Warehouse'
        db.delete_table('products_warehouse')

        # Deleting model 'BalanceLog'
        db.delete_table('products_balancelog')

        # Deleting model 'BalanceLogEntry'
        db.delete_table('products_balancelogentry')


    models = {
        'products.balancelog': {
            'Meta': {'object_name': 'BalanceLog', 'unique_together': "(['product', 'warehouse'],)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Warehouse']"})
        },
        'products.balancelogentry': {
            'Meta': {'object_name': 'BalanceLogEntry'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'balance_log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.BalanceLog']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'products.pricelist': {
            'Meta': {'object_name': 'Pricelist'},
            'base': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['products.Pricelist']", 'blank': 'True'}),
            'base_derivation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'products.pricelistentry': {
            'Meta': {'object_name': 'PricelistEntry', 'unique_together': "(['pricelist', 'product'],)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'}),
            'pricelist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Pricelist']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"})
        },
        'products.product': {
            'Meta': {'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'products.uom': {
            'Meta': {'object_name': 'Uom'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'products.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        }
    }

    complete_apps = ['products']