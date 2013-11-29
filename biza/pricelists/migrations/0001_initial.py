# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pricelist'
        db.create_table(u'pricelists_pricelist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('base_pricelist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricelists.Pricelist'], null=True, blank=True)),
            ('is_tax_included', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_so_pricelist', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('enforce_price_limit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price_precision', self.gf('django.db.models.fields.SmallIntegerField')(default=2)),
        ))
        db.send_create_signal(u'pricelists', ['Pricelist'])


    def backwards(self, orm):
        # Deleting model 'Pricelist'
        db.delete_table(u'pricelists_pricelist')


    models = {
        u'pricelists.pricelist': {
            'Meta': {'object_name': 'Pricelist'},
            'base_pricelist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pricelists.Pricelist']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enforce_price_limit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_so_pricelist': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_tax_included': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'price_precision': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'})
        }
    }

    complete_apps = ['pricelists']