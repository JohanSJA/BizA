# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Unit.abbreviation'
        db.delete_column(u'stocks_unit', 'abbreviation')

        # Adding field 'Balance.reason'
        db.add_column(u'stocks_balance', 'reason',
                      self.gf('django.db.models.fields.CharField')(default='T', max_length=1),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Unit.abbreviation'
        raise RuntimeError("Cannot reverse this migration. 'Unit.abbreviation' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Unit.abbreviation'
        db.add_column(u'stocks_unit', 'abbreviation',
                      self.gf('django.db.models.fields.CharField')(max_length=3, unique=True),
                      keep_default=False)

        # Deleting field 'Balance.reason'
        db.delete_column(u'stocks_balance', 'reason')


    models = {
        u'stocks.balance': {
            'Meta': {'object_name': 'Balance'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'changes': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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