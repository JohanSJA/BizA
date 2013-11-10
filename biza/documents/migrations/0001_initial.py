# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'documents_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('length', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'documents', ['Document'])

        # Adding model 'Version'
        db.create_table(u'documents_version', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Document'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'documents', ['Version'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'documents_document')

        # Deleting model 'Version'
        db.delete_table(u'documents_version')


    models = {
        u'documents.document': {
            'Meta': {'object_name': 'Document'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.SmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'documents.version': {
            'Meta': {'object_name': 'Version'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['documents']