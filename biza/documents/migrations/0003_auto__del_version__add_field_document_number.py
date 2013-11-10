# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Version'
        db.delete_table(u'documents_version')

        # Adding field 'Document.number'
        db.add_column(u'documents_document', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Version'
        db.create_table(u'documents_version', (
            ('number', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('document', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documents.Document'], unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'documents', ['Version'])

        # Deleting field 'Document.number'
        db.delete_column(u'documents_document', 'number')


    models = {
        u'documents.document': {
            'Meta': {'object_name': 'Document'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.SmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['documents']