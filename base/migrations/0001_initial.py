# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AmmoCover'
        db.create_table(u'base_ammocover', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cover_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cover_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('cover_material', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('cover_length', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['AmmoCover'])

        # Adding unique constraint on 'AmmoCover', fields ['cover_weight', 'cover_type', 'cover_material', 'cover_length']
        db.create_unique(u'base_ammocover', ['cover_weight', 'cover_type', 'cover_material', 'cover_length'])

        # Adding model 'AmmoGunpowder'
        db.create_table(u'base_ammogunpowder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gunpowder_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('gunpowder_color', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'base', ['AmmoGunpowder'])

        # Adding unique constraint on 'AmmoGunpowder', fields ['gunpowder_type', 'gunpowder_color']
        db.create_unique(u'base_ammogunpowder', ['gunpowder_type', 'gunpowder_color'])

        # Adding model 'AmmoProjectile'
        db.create_table(u'base_ammoprojectile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projectile_diameter', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('projectile_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('projectile_material', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('sulco_serrilhado', self.gf('django.db.models.fields.CharField')(default='0', max_length=1, blank=True)),
            ('has_magnetic_properties', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'base', ['AmmoProjectile'])

        # Adding unique constraint on 'AmmoProjectile', fields ['projectile_diameter', 'projectile_weight', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties']
        db.create_unique(u'base_ammoprojectile', ['projectile_diameter', 'projectile_weight', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties'])

        # Adding model 'AmmoTip'
        db.create_table(u'base_ammotip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tip_color', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('tip_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('tip_shape', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'base', ['AmmoTip'])

        # Adding unique constraint on 'AmmoTip', fields ['tip_color', 'tip_type', 'tip_shape']
        db.create_unique(u'base_ammotip', ['tip_color', 'tip_type', 'tip_shape'])

        # Adding model 'Ammo'
        db.create_table(u'base_ammo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('head_stamp', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('ammo_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('varnish_color', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('total_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('percussion_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('factory', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.AmmoTip'], null=True, blank=True)),
            ('projectile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.AmmoProjectile'], null=True, blank=True)),
            ('cover', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.AmmoCover'], null=True, blank=True)),
            ('gunpowder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.AmmoGunpowder'], null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['Ammo'])

        # Adding M2M table for field photos on 'Ammo'
        db.create_table(u'base_ammo_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ammo', models.ForeignKey(orm[u'base.ammo'], null=False)),
            ('photo', models.ForeignKey(orm[u'photologue.photo'], null=False))
        ))
        db.create_unique(u'base_ammo_photos', ['ammo_id', 'photo_id'])

        # Adding model 'AmmoCaliber'
        db.create_table(u'base_ammocaliber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ammo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='calibers', to=orm['base.Ammo'])),
            ('caliber_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('caliber_value', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal(u'base', ['AmmoCaliber'])

        # Adding unique constraint on 'AmmoCaliber', fields ['caliber_type', 'caliber_value']
        db.create_unique(u'base_ammocaliber', ['caliber_type', 'caliber_value'])


    def backwards(self, orm):
        # Removing unique constraint on 'AmmoCaliber', fields ['caliber_type', 'caliber_value']
        db.delete_unique(u'base_ammocaliber', ['caliber_type', 'caliber_value'])

        # Removing unique constraint on 'AmmoTip', fields ['tip_color', 'tip_type', 'tip_shape']
        db.delete_unique(u'base_ammotip', ['tip_color', 'tip_type', 'tip_shape'])

        # Removing unique constraint on 'AmmoProjectile', fields ['projectile_diameter', 'projectile_weight', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties']
        db.delete_unique(u'base_ammoprojectile', ['projectile_diameter', 'projectile_weight', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties'])

        # Removing unique constraint on 'AmmoGunpowder', fields ['gunpowder_type', 'gunpowder_color']
        db.delete_unique(u'base_ammogunpowder', ['gunpowder_type', 'gunpowder_color'])

        # Removing unique constraint on 'AmmoCover', fields ['cover_weight', 'cover_type', 'cover_material', 'cover_length']
        db.delete_unique(u'base_ammocover', ['cover_weight', 'cover_type', 'cover_material', 'cover_length'])

        # Deleting model 'AmmoCover'
        db.delete_table(u'base_ammocover')

        # Deleting model 'AmmoGunpowder'
        db.delete_table(u'base_ammogunpowder')

        # Deleting model 'AmmoProjectile'
        db.delete_table(u'base_ammoprojectile')

        # Deleting model 'AmmoTip'
        db.delete_table(u'base_ammotip')

        # Deleting model 'Ammo'
        db.delete_table(u'base_ammo')

        # Removing M2M table for field photos on 'Ammo'
        db.delete_table('base_ammo_photos')

        # Deleting model 'AmmoCaliber'
        db.delete_table(u'base_ammocaliber')


    models = {
        u'base.ammo': {
            'Meta': {'object_name': 'Ammo'},
            'ammo_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.AmmoCover']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'factory': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
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
            'varnish_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
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
            'Meta': {'unique_together': "(('gunpowder_type', 'gunpowder_color'),)", 'object_name': 'AmmoGunpowder'},
            'gunpowder_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'gunpowder_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.ammoprojectile': {
            'Meta': {'unique_together': "(('projectile_diameter', 'projectile_weight', 'projectile_material', 'sulco_serrilhado', 'has_magnetic_properties'),)", 'object_name': 'AmmoProjectile'},
            'has_magnetic_properties': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projectile_diameter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'projectile_material': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
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