# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shop'
        db.create_table(u'retails_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('warehouse', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['stocks.Warehouse'], unique=True)),
        ))
        db.send_create_signal(u'retails', ['Shop'])

        # Adding model 'Worker'
        db.create_table(u'retails_worker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Shop'])),
            ('worker', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'retails', ['Worker'])

        # Adding model 'Price'
        db.create_table(u'retails_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['stocks.Stock'], unique=True)),
            ('base', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
            ('lowest', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal(u'retails', ['Price'])

        # Adding model 'Sale'
        db.create_table(u'retails_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Shop'])),
            ('closed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('closed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'retails', ['Sale'])

        # Adding model 'Line'
        db.create_table(u'retails_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['retails.Sale'])),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Stock'])),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'retails', ['Line'])

        # Adding model 'Receipt'
        db.create_table(u'retails_receipt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sale', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['retails.Sale'], unique=True)),
        ))
        db.send_create_signal(u'retails', ['Receipt'])


    def backwards(self, orm):
        # Deleting model 'Shop'
        db.delete_table(u'retails_shop')

        # Deleting model 'Worker'
        db.delete_table(u'retails_worker')

        # Deleting model 'Price'
        db.delete_table(u'retails_price')

        # Deleting model 'Sale'
        db.delete_table(u'retails_sale')

        # Deleting model 'Line'
        db.delete_table(u'retails_line')

        # Deleting model 'Receipt'
        db.delete_table(u'retails_receipt')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'retails.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Sale']"}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Stock']"}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'})
        },
        u'retails.price': {
            'Meta': {'object_name': 'Price'},
            'base': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lowest': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'stock': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['stocks.Stock']", 'unique': 'True'})
        },
        u'retails.receipt': {
            'Meta': {'object_name': 'Receipt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sale': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['retails.Sale']", 'unique': 'True'})
        },
        u'retails.sale': {
            'Meta': {'object_name': 'Sale'},
            'closed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'closed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Shop']"})
        },
        u'retails.shop': {
            'Meta': {'object_name': 'Shop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'warehouse': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['stocks.Warehouse']", 'unique': 'True'})
        },
        u'retails.worker': {
            'Meta': {'object_name': 'Worker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['retails.Shop']"}),
            'worker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discontinued': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Unit']"})
        },
        u'stocks.unit': {
            'Meta': {'object_name': 'Unit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['retails']