# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Version.document'
        db.alter_column(u'documents_version', 'document_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['documents.Document'], unique=True))
        # Adding unique constraint on 'Version', fields ['document']
        db.create_unique(u'documents_version', ['document_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Version', fields ['document']
        db.delete_unique(u'documents_version', ['document_id'])


        # Changing field 'Version.document'
        db.alter_column(u'documents_version', 'document_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Document']))

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
            'document': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['documents.Document']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['documents']