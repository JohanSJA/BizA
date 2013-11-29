# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Uom'
        db.create_table(u'uoms_uom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'uoms', ['Uom'])


    def backwards(self, orm):
        # Deleting model 'Uom'
        db.delete_table(u'uoms_uom')


    models = {
        u'uoms.uom': {
            'Meta': {'object_name': 'Uom'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['uoms']