# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pricelist'
        db.create_table('pricelists_pricelist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('base', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['pricelists.Pricelist'], blank=True)),
            ('base_derivation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pricelists', ['Pricelist'])

        # Adding model 'PricelistEntry'
        db.create_table('pricelists_pricelistentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pricelist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricelists.Pricelist'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=4, max_digits=12)),
        ))
        db.send_create_signal('pricelists', ['PricelistEntry'])

        # Adding unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.create_unique('pricelists_pricelistentry', ['pricelist_id', 'product_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.delete_unique('pricelists_pricelistentry', ['pricelist_id', 'product_id'])

        # Deleting model 'Pricelist'
        db.delete_table('pricelists_pricelist')

        # Deleting model 'PricelistEntry'
        db.delete_table('pricelists_pricelistentry')


    models = {
        'pricelists.pricelist': {
            'Meta': {'object_name': 'Pricelist'},
            'base': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['pricelists.Pricelist']", 'blank': 'True'}),
            'base_derivation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'pricelists.pricelistentry': {
            'Meta': {'unique_together': "(['pricelist', 'product'],)", 'object_name': 'PricelistEntry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'}),
            'pricelist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricelists.Pricelist']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"})
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
        }
    }

    complete_apps = ['pricelists']