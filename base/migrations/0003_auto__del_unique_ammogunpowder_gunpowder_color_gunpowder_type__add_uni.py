# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'AmmoProjectile', fields ['projectile_material', 'projectile_weight', 'projectile_diameter', 'has_magnetic_properties', 'sulco_serrilhado']
        db.delete_unique(u'base_ammoprojectile', ['projectile_material', 'projectile_weight', 'projectile_diameter', 'has_magnetic_properties', 'sulco_serrilhado'])

        # Removing unique constraint on 'AmmoGunpowder', fields ['gunpowder_color', 'gunpowder_type']
        db.delete_unique(u'base_ammogunpowder', ['gunpowder_color', 'gunpowder_type'])

        # Adding unique constraint on 'AmmoGunpowder', fields ['gunpowder_weight', 'gunpowder_color', 'gunpowder_type']
        db.create_unique(u'base_ammogunpowder', ['gunpowder_weight', 'gunpowder_color', 'gunpowder_type'])

        # Adding unique constraint on 'AmmoProjectile', fields ['projectile_diameter', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties', 'projectile_weight', 'projectile_varnish_color']
        db.create_unique(u'base_ammoprojectile', ['projectile_diameter', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties', 'projectile_weight', 'projectile_varnish_color'])


    def backwards(self, orm):
        # Removing unique constraint on 'AmmoProjectile', fields ['projectile_diameter', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties', 'projectile_weight', 'projectile_varnish_color']
        db.delete_unique(u'base_ammoprojectile', ['projectile_diameter', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties', 'projectile_weight', 'projectile_varnish_color'])

        # Removing unique constraint on 'AmmoGunpowder', fields ['gunpowder_weight', 'gunpowder_color', 'gunpowder_type']
        db.delete_unique(u'base_ammogunpowder', ['gunpowder_weight', 'gunpowder_color', 'gunpowder_type'])

        # Adding unique constraint on 'AmmoGunpowder', fields ['gunpowder_color', 'gunpowder_type']
        db.create_unique(u'base_ammogunpowder', ['gunpowder_color', 'gunpowder_type'])

        # Adding unique constraint on 'AmmoProjectile', fields ['projectile_material', 'projectile_weight', 'projectile_diameter', 'has_magnetic_properties', 'sulco_serrilhado']
        db.create_unique(u'base_ammoprojectile', ['projectile_material', 'projectile_weight', 'projectile_diameter', 'has_magnetic_properties', 'sulco_serrilhado'])


    models = {
        u'base.ammo': {
            'Meta': {'object_name': 'Ammo'},
            'ammo_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.AmmoCover']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'factory': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'fulminant_varnish_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'gunpowder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.AmmoGunpowder']", 'null': 'True', 'blank': 'True'}),
            'head_stamp': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percussion_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photologue.Photo']", 'symmetrical': 'False'}),
            'projectile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.AmmoProjectile']", 'null': 'True', 'blank': 'True'}),
            'tip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.AmmoTip']", 'null': 'True', 'blank': 'True'}),
            'total_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'base.ammocaliber': {
            'Meta': {'unique_together': "(('caliber_type', 'caliber_value'),)", 'object_name': 'AmmoCaliber'},
            'ammo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'calibers'", 'to': u"orm['base.Ammo']"}),
            'caliber_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'caliber_value': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.ammocover': {
            'Meta': {'unique_together': "(('cover_weight', 'cover_type', 'cover_material', 'cover_length'),)", 'object_name': 'AmmoCover'},
            'cover_length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cover_material': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'cover_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'cover_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.ammogunpowder': {
            'Meta': {'unique_together': "(('gunpowder_type', 'gunpowder_color', 'gunpowder_weight'),)", 'object_name': 'AmmoGunpowder'},
            'gunpowder_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'gunpowder_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'gunpowder_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.ammoprojectile': {
            'Meta': {'unique_together': "(('projectile_diameter', 'projectile_weight', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties', 'projectile_varnish_color'),)", 'object_name': 'AmmoProjectile'},
            'has_magnetic_properties': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projectile_diameter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'projectile_material': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'projectile_varnish_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'projectile_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sulco_serrilhado': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'blank': 'True'})
        },
        u'base.ammotip': {
            'Meta': {'unique_together': "(('tip_color', 'tip_type', 'tip_shape'),)", 'object_name': 'AmmoTip'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tip_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'tip_shape': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'tip_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'})
        },
        u'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        }
    }

    complete_apps = ['base']