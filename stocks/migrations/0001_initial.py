# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unit'
        db.create_table(u'stocks_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
        ))
        db.send_create_signal(u'stocks', ['Unit'])

        # Adding model 'Stock'
        db.create_table(u'stocks_stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Unit'])),
            ('discontinued', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'stocks', ['Stock'])

        # Adding model 'Warehouse'
        db.create_table(u'stocks_warehouse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'stocks', ['Warehouse'])

        # Adding model 'Balance'
        db.create_table(u'stocks_balance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Stock'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
            ('changes', self.gf('django.db.models.fields.IntegerField')()),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'stocks', ['Balance'])


    def backwards(self, orm):
        # Deleting model 'Unit'
        db.delete_table(u'stocks_unit')

        # Deleting model 'Stock'
        db.delete_table(u'stocks_stock')

        # Deleting model 'Warehouse'
        db.delete_table(u'stocks_warehouse')

        # Deleting model 'Balance'
        db.delete_table(u'stocks_balance')


    models = {
        u'stocks.balance': {
            'Meta': {'object_name': 'Balance'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'changes': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Stock']"}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Warehouse']"})
        },
        u'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discontinued': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Unit']"})
        },
        u'stocks.unit': {
            'Meta': {'object_name': 'Unit'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['stocks']