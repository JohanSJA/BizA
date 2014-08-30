# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting unique constraints on 'BalanceLog'
        db.delete_unique('products_balancelog', ['product_id', 'warehouse_id'])

        # Adding model 'Warehouse'
        db.rename_table('products_warehouse', 'balances_warehouse')

        # Adding model 'BalanceLog'
        db.rename_table('products_balancelog', 'balances_balancelog')

        # Adding unique constraint on 'BalanceLog', fields ['product', 'warehouse']
        db.create_unique('balances_balancelog', ['product_id', 'warehouse_id'])

        # Adding model 'BalanceLogEntry'
        db.rename_table('products_balancelogentry', 'balances_balancelogentry')

        if not db.dry_run:
            orm['contenttypes.contenttype'].objects.filter(app_label='products', model='warehouse').update(app_label='balances')
            orm['contenttypes.contenttype'].objects.filter(app_label='products', model='balancelog').update(app_label='balances')
            orm['contenttypes.contenttype'].objects.filter(app_label='products', model='balancelogentry').update(app_label='balances')


    def backwards(self, orm):
        # Deleting unique constraints on 'BalanceLog'
        db.delete_unique('balances_balancelog', ['product_id', 'warehouse_id'])

        # Adding model 'Warehouse'
        db.rename_table('balances_warehouse', 'products_warehouse')

        # Adding model 'BalanceLog'
        db.rename_table('balances_balancelog', 'products_balancelog')

        # Adding unique constraint on 'BalanceLog', fields ['product', 'warehouse']
        db.create_unique('products_balancelog', ['product_id', 'warehouse_id'])

        # Adding model 'BalanceLogEntry'
        db.rename_table('balances_balancelogentry', 'products_balancelogentry')

        if not db.dry_run:
            orm['contenttypes.contenttype'].objects.filter(app_label='balances', model='warehouse').update(app_label='products')
            orm['contenttypes.contenttype'].objects.filter(app_label='balances', model='balancelog').update(app_label='products')
            orm['contenttypes.contenttype'].objects.filter(app_label='balances', model='balancelogentry').update(app_label='products')


    models = {
        'balances.balancelog': {
            'Meta': {'unique_together': "(['product', 'warehouse'],)", 'object_name': 'BalanceLog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['balances.Warehouse']"})
        },
        'balances.balancelogentry': {
            'Meta': {'object_name': 'BalanceLogEntry'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'balance_log': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['balances.BalanceLog']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'balances.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'products.product': {
            'Meta': {'ordering': "['model']", 'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['contenttypes', 'balances']
