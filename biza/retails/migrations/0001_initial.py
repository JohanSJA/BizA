# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table(u'retails_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
        ))
        db.send_create_signal(u'retails', ['Store'])

        # Adding model 'Saleperson'
        db.create_table(u'retails_saleperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'retails', ['Saleperson'])

        # Adding model 'Sale'
        db.create_table(u'retails_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Store'])),
            ('saleperson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Saleperson'])),
            ('opening_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('closing_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'retails', ['Sale'])

        # Adding model 'SaleLine'
        db.create_table(u'retails_saleline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Sale'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('discount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
        ))
        db.send_create_signal(u'retails', ['SaleLine'])

        # Adding unique constraint on 'SaleLine', fields ['sale', 'product']
        db.create_unique(u'retails_saleline', ['sale_id', 'product_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SaleLine', fields ['sale', 'product']
        db.delete_unique(u'retails_saleline', ['sale_id', 'product_id'])

        # Deleting model 'Store'
        db.delete_table(u'retails_store')

        # Deleting model 'Saleperson'
        db.delete_table(u'retails_saleperson')

        # Deleting model 'Sale'
        db.delete_table(u'retails_sale')

        # Deleting model 'SaleLine'
        db.delete_table(u'retails_saleline')


    models = {
        u'retails.sale': {
            'Meta': {'object_name': 'Sale'},
            'closing_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'saleperson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Saleperson']"}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Store']"})
        },
        u'retails.saleline': {
            'Meta': {'unique_together': "(['sale', 'product'],)", 'object_name': 'SaleLine'},
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Sale']"})
        },
        u'retails.saleperson': {
            'Meta': {'object_name': 'Saleperson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'retails.store': {
            'Meta': {'object_name': 'Store'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Warehouse']"})
        },
        u'stocks.product': {
            'Meta': {'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lowest_retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'lowest_wholesale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
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