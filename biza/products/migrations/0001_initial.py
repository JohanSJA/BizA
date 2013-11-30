# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unit'
        db.create_table(u'products_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('allow_fraction', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'products', ['Unit'])

        # Adding model 'Category'
        db.create_table(u'products_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
        ))
        db.send_create_signal(u'products', ['Category'])

        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('barcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Unit'])),
        ))
        db.send_create_signal(u'products', ['Product'])

        # Adding model 'Price'
        db.create_table(u'products_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=4)),
            ('base', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('lowest', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal(u'products', ['Price'])

        # Adding model 'BasePrice'
        db.create_table(u'products_baseprice', (
            (u'price_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Price'], unique=True, primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Product'], unique=True)),
        ))
        db.send_create_signal(u'products', ['BasePrice'])

        # Adding model 'BranchPrice'
        db.create_table(u'products_branchprice', (
            (u'price_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Price'], unique=True, primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['branches.Branch'])),
        ))
        db.send_create_signal(u'products', ['BranchPrice'])


    def backwards(self, orm):
        # Deleting model 'Unit'
        db.delete_table(u'products_unit')

        # Deleting model 'Category'
        db.delete_table(u'products_category')

        # Deleting model 'Product'
        db.delete_table(u'products_product')

        # Deleting model 'Price'
        db.delete_table(u'products_price')

        # Deleting model 'BasePrice'
        db.delete_table(u'products_baseprice')

        # Deleting model 'BranchPrice'
        db.delete_table(u'products_branchprice')


    models = {
        u'branches.branch': {
            'Meta': {'object_name': 'Branch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'products.baseprice': {
            'Meta': {'object_name': 'BasePrice', '_ormbases': [u'products.Price']},
            u'price_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['products.Price']", 'unique': 'True', 'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['products.Product']", 'unique': 'True'})
        },
        u'products.branchprice': {
            'Meta': {'object_name': 'BranchPrice', '_ormbases': [u'products.Price']},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['branches.Branch']"}),
            u'price_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['products.Price']", 'unique': 'True', 'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"})
        },
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"})
        },
        u'products.price': {
            'Meta': {'object_name': 'Price'},
            'base': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lowest': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Unit']"})
        },
        u'products.unit': {
            'Meta': {'object_name': 'Unit'},
            'allow_fraction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['products']