# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Branch'
        db.create_table(u'branches_branch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'branches', ['Branch'])

        # Adding model 'Station'
        db.create_table(u'branches_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['branches.Branch'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'branches', ['Station'])

        # Adding unique constraint on 'Station', fields ['branch', 'name']
        db.create_unique(u'branches_station', ['branch_id', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Station', fields ['branch', 'name']
        db.delete_unique(u'branches_station', ['branch_id', 'name'])

        # Deleting model 'Branch'
        db.delete_table(u'branches_branch')

        # Deleting model 'Station'
        db.delete_table(u'branches_station')


    models = {
        u'branches.branch': {
            'Meta': {'object_name': 'Branch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'branches.station': {
            'Meta': {'unique_together': "(('branch', 'name'),)", 'object_name': 'Station'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['branches.Branch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['branches']