# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pricelist'
        db.create_table('prices_pricelist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('markup_from', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prices.Pricelist'], blank=True, null=True)),
            ('markup_percentage', self.gf('django.db.models.fields.SmallIntegerField')(blank=True, null=True)),
        ))
        db.send_create_signal('prices', ['Pricelist'])

        # Adding model 'PricelistEntry'
        db.create_table('prices_pricelistentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pricelist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prices.Pricelist'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal('prices', ['PricelistEntry'])

        # Adding unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.create_unique('prices_pricelistentry', ['pricelist_id', 'product_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.delete_unique('prices_pricelistentry', ['pricelist_id', 'product_id'])

        # Deleting model 'Pricelist'
        db.delete_table('prices_pricelist')

        # Deleting model 'PricelistEntry'
        db.delete_table('prices_pricelistentry')


    models = {
        'prices.pricelist': {
            'Meta': {'object_name': 'Pricelist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markup_from': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prices.Pricelist']", 'blank': 'True', 'null': 'True'}),
            'markup_percentage': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'prices.pricelistentry': {
            'Meta': {'unique_together': "(['pricelist', 'product'],)", 'object_name': 'PricelistEntry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'pricelist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prices.Pricelist']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"})
        },
        'products.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'products.product': {
            'Meta': {'ordering': "['code']", 'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'unique': 'True', 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['prices']