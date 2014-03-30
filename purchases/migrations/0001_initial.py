# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Supplier'
        db.create_table('purchases_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('partner', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['partners.Partner'])),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
        ))
        db.send_create_signal('purchases', ['Supplier'])


    def backwards(self, orm):
        # Deleting model 'Supplier'
        db.delete_table('purchases_supplier')


    models = {
        'partners.partner': {
            'Meta': {'object_name': 'Partner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'purchases.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['partners.Partner']"})
        }
    }

    complete_apps = ['purchases']