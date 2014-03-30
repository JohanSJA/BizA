# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Partner'
        db.create_table('partners_partner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
        ))
        db.send_create_signal('partners', ['Partner'])

        # Adding model 'Address'
        db.create_table('partners_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partners.Partner'])),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('partners', ['Address'])

        # Adding unique constraint on 'Address', fields ['partner', 'function']
        db.create_unique('partners_address', ['partner_id', 'function'])

        # Adding model 'ContactMethod'
        db.create_table('partners_contactmethod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partners.Partner'])),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('information', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('partners', ['ContactMethod'])


    def backwards(self, orm):
        # Removing unique constraint on 'Address', fields ['partner', 'function']
        db.delete_unique('partners_address', ['partner_id', 'function'])

        # Deleting model 'Partner'
        db.delete_table('partners_partner')

        # Deleting model 'Address'
        db.delete_table('partners_address')

        # Deleting model 'ContactMethod'
        db.delete_table('partners_contactmethod')


    models = {
        'partners.address': {
            'Meta': {'object_name': 'Address', 'unique_together': "(['partner', 'function'],)"},
            'address': ('django.db.models.fields.TextField', [], {}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Partner']"})
        },
        'partners.contactmethod': {
            'Meta': {'object_name': 'ContactMethod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Partner']"})
        },
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        }
    }

    complete_apps = ['partners']