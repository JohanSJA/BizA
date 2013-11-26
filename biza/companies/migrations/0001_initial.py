# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'companies_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('reg_num', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('tel', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'companies', ['Company'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'companies_company')


    models = {
        u'companies.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reg_num': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'tel': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['companies']