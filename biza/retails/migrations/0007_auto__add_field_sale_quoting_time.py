# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sale.quoting_time'
        db.add_column(u'retails_sale', 'quoting_time',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sale.quoting_time'
        db.delete_column(u'retails_sale', 'quoting_time')


    models = {
        u'retails.sale': {
            'Meta': {'ordering': "['-opening_time']", 'object_name': 'Sale'},
            'cash_bill_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'closing_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'quotation_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'quoting_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'saleperson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Saleperson']"}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Store']"})
        },
        u'retails.saleline': {
            'Meta': {'unique_together': "(['sale', 'product'],)", 'object_name': 'SaleLine'},
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Sale']"}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'})
        },
        u'retails.saleperson': {
            'Meta': {'object_name': 'Saleperson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'retails.store': {
            'Meta': {'object_name': 'Store'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Warehouse']"})
        },
        u'stocks.product': {
            'Meta': {'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lowest_retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'lowest_wholesale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'wholesale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'})
        },
        u'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['retails']