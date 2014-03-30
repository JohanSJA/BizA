# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Salesman'
        db.create_table('wholesales_salesman', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('wholesales', ['Salesman'])

        # Adding model 'Customer'
        db.create_table('wholesales_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partners.Partner'], unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True)),
            ('served_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wholesales.Salesman'])),
        ))
        db.send_create_signal('wholesales', ['Customer'])


    def backwards(self, orm):
        # Deleting model 'Salesman'
        db.delete_table('wholesales_salesman')

        # Deleting model 'Customer'
        db.delete_table('wholesales_customer')


    models = {
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'wholesales.customer': {
            'Meta': {'object_name': 'Customer'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['partners.Partner']", 'unique': 'True'}),
            'served_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wholesales.Salesman']"})
        },
        'wholesales.salesman': {
            'Meta': {'object_name': 'Salesman'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wholesales']