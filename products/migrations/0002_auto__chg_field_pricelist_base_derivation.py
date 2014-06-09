# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Pricelist.base_derivation'
        db.alter_column('products_pricelist', 'base_derivation', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Pricelist.base_derivation'
        db.alter_column('products_pricelist', 'base_derivation', self.gf('django.db.models.fields.IntegerField')(null=True))

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
            'base': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Pricelist']", 'blank': 'True', 'null': 'True'}),
            'base_derivation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'products.pricelistentry': {
            'Meta': {'object_name': 'PricelistEntry', 'unique_together': "(['pricelist', 'product'],)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'pricelist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Pricelist']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"})
        },
        'products.product': {
            'Meta': {'object_name': 'Product', 'ordering': "['model']"},
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