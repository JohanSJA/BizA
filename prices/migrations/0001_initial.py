# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Remove unique constraints on "PricelistEntry"
        db.delete_unique("products_pricelistentry", ["pricelist_id", "product_id"])

        # Adding model 'Pricelist'
        db.rename_table("products_pricelist", "prices_pricelist")
        db.alter_column("prices_pricelist", "base", models.ForeignKey(orm["prices.Pricelist"], null=True, blank=True), explicit_name=False)

        # Adding model 'PricelistEntry'
        db.rename_table("products_pricelistentry", "prices_pricelistentry")
        db.alter_column("prices_pricelistentry", "pricelist", models.ForeignKey(orm["prices.Pricelist"]), explicit_name=False)

        # Adding unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.create_unique('prices_pricelistentry', ['pricelist_id', 'product_id'])

        if not db.dry_run:
            orm["contenttypes.contenttype"].objects.filter(app_label="products", model="pricelist").update(app_label="prices")
            orm["contenttypes.contenttype"].objects.filter(app_label="products", model="pricelistentry").update(app_label="prices")


    def backwards(self, orm):
        # Remove unique constraints on "PricelistEntry"
        db.delete_unique("prices_pricelistentry", ["pricelist_id", "product_id"])

        # Adding model 'Pricelist'
        db.rename_table("prices_pricelist", "products_pricelist")
        db.alter_column("prices_pricelist", "base", models.ForeignKey(orm["products.Pricelist"], null=True, blank=True), explicit_name=False)

        # Adding model 'PricelistEntry'
        db.rename_table("prices_pricelistentry", "products_pricelistentry")
        db.alter_column("prices_pricelistentry", "pricelist", models.ForeignKey(orm["products.Pricelist"]), explicit_name=False)

        # Adding unique constraint on 'PricelistEntry', fields ['pricelist', 'product']
        db.create_unique('products_pricelistentry', ['pricelist_id', 'product_id'])

        if not db.dry_run:
            orm["contenttypes.contenttype"].objects.filter(app_label="prices", model="pricelist").update(app_label="products")
            orm["contenttypes.contenttype"].objects.filter(app_label="prices", model="pricelistentry").update(app_label="products")


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'prices.pricelist': {
            'Meta': {'object_name': 'Pricelist'},
            'base': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['prices.Pricelist']", 'blank': 'True'}),
            'base_derivation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'prices.pricelistentry': {
            'Meta': {'unique_together': "(['pricelist', 'product'],)", 'object_name': 'PricelistEntry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '4', 'max_digits': '12'}),
            'pricelist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prices.Pricelist']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"})
        },
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'})
        },
        'products.product': {
            'Meta': {'ordering': "['model']", 'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['contenttypes', 'prices']
