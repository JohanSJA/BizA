# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unit'
        db.create_table(u'sellables_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('allow_fraction', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sellables', ['Unit'])

        # Adding model 'TaxConstant'
        db.create_table(u'sellables_taxconstant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tax_type', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tax_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'sellables', ['TaxConstant'])

        # Adding model 'Category'
        db.create_table(u'sellables_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('commission', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sellables.Category'])),
            ('tax_constant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sellables.TaxConstant'])),
        ))
        db.send_create_signal(u'sellables', ['Category'])

        # Adding model 'Sellable'
        db.create_table(u'sellables_sellable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('barcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=4)),
            ('base_price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('max_discount', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('commission', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sellables.Unit'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sellables.Category'])),
            ('tax_constant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sellables.TaxConstant'])),
        ))
        db.send_create_signal(u'sellables', ['Sellable'])


    def backwards(self, orm):
        # Deleting model 'Unit'
        db.delete_table(u'sellables_unit')

        # Deleting model 'TaxConstant'
        db.delete_table(u'sellables_taxconstant')

        # Deleting model 'Category'
        db.delete_table(u'sellables_category')

        # Deleting model 'Sellable'
        db.delete_table(u'sellables_sellable')


    models = {
        u'sellables.category': {
            'Meta': {'object_name': 'Category'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'commission': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sellables.Category']"}),
            'tax_constant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sellables.TaxConstant']"})
        },
        u'sellables.sellable': {
            'Meta': {'object_name': 'Sellable'},
            'barcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'base_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sellables.Category']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'commission': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '4'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_discount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tax_constant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sellables.TaxConstant']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sellables.Unit']"})
        },
        u'sellables.taxconstant': {
            'Meta': {'object_name': 'TaxConstant'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'tax_type': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tax_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'sellables.unit': {
            'Meta': {'object_name': 'Unit'},
            'allow_fraction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['sellables']