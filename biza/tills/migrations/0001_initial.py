# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Till'
        db.create_table(u'tills_till', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['branches.Station'])),
            ('opening_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('closing_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('initial_cash_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('final_cash_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'tills', ['Till'])

        # Adding model 'Entry'
        db.create_table(u'tills_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('till', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tills.Till'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal(u'tills', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Till'
        db.delete_table(u'tills_till')

        # Deleting model 'Entry'
        db.delete_table(u'tills_entry')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'branches.branch': {
            'Meta': {'object_name': 'Branch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employees.Employee']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'branches.station': {
            'Meta': {'unique_together': "(('branch', 'name'),)", 'object_name': 'Station'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['branches.Branch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employees.employee': {
            'Meta': {'object_name': 'Employee'},
            'admission_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'tills.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'till': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tills.Till']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        },
        u'tills.till': {
            'Meta': {'object_name': 'Till'},
            'closing_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'final_cash_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_cash_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'opening_time': ('django.db.models.fields.DateTimeField', [], {}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['branches.Station']"}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['tills']