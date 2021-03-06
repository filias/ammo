# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'base_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('country_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal(u'base', ['Country'])

        # Adding model 'Ammo'
        db.create_table(u'base_ammo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('head_stamp', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('ammo_type', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('primer_varnish_color', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('total_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('percussion_type', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Country'], null=True, blank=True)),
            ('factory', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('projectile_diameter', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('projectile_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('projectile_material', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('serrated', self.gf('django.db.models.fields.CharField')(default='0', max_length=1, blank=True)),
            ('has_magnetic_properties', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('projectile_varnish_color', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('tip_color', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('tip_type', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('tip_shape', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('gunpowder_type', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('gunpowder_color', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('gunpowder_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('casing_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('casing_type', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('casing_material', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('casing_length', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['Ammo'])

        # Adding unique constraint on 'Ammo', fields ['name', 'head_stamp', 'year', 'ammo_type', 'primer_varnish_color', 'total_weight', 'percussion_type', 'projectile_diameter', 'projectile_weight', 'projectile_material', 'serrated', 'has_magnetic_properties', 'projectile_varnish_color', 'tip_color', 'tip_type', 'tip_shape', 'gunpowder_type', 'gunpowder_weight', 'gunpowder_color', 'casing_weight', 'casing_type', 'casing_material', 'casing_length']
        db.create_unique(u'base_ammo', ['name', 'head_stamp', 'year', 'ammo_type', 'primer_varnish_color', 'total_weight', 'percussion_type', 'projectile_diameter', 'projectile_weight', 'projectile_material', 'serrated', 'has_magnetic_properties', 'projectile_varnish_color', 'tip_color', 'tip_type', 'tip_shape', 'gunpowder_type', 'gunpowder_weight', 'gunpowder_color', 'casing_weight', 'casing_type', 'casing_material', 'casing_length'])

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

        # Adding unique constraint on 'AmmoCaliber', fields ['ammo', 'caliber_type', 'caliber_value']
        db.create_unique(u'base_ammocaliber', ['ammo_id', 'caliber_type', 'caliber_value'])


    def backwards(self, orm):
        # Removing unique constraint on 'AmmoCaliber', fields ['ammo', 'caliber_type', 'caliber_value']
        db.delete_unique(u'base_ammocaliber', ['ammo_id', 'caliber_type', 'caliber_value'])

        # Removing unique constraint on 'Ammo', fields ['name', 'head_stamp', 'year', 'ammo_type', 'primer_varnish_color', 'total_weight', 'percussion_type', 'projectile_diameter', 'projectile_weight', 'projectile_material', 'serrated', 'has_magnetic_properties', 'projectile_varnish_color', 'tip_color', 'tip_type', 'tip_shape', 'gunpowder_type', 'gunpowder_weight', 'gunpowder_color', 'casing_weight', 'casing_type', 'casing_material', 'casing_length']
        db.delete_unique(u'base_ammo', ['name', 'head_stamp', 'year', 'ammo_type', 'primer_varnish_color', 'total_weight', 'percussion_type', 'projectile_diameter', 'projectile_weight', 'projectile_material', 'serrated', 'has_magnetic_properties', 'projectile_varnish_color', 'tip_color', 'tip_type', 'tip_shape', 'gunpowder_type', 'gunpowder_weight', 'gunpowder_color', 'casing_weight', 'casing_type', 'casing_material', 'casing_length'])

        # Deleting model 'Country'
        db.delete_table(u'base_country')

        # Deleting model 'Ammo'
        db.delete_table(u'base_ammo')

        # Removing M2M table for field photos on 'Ammo'
        db.delete_table('base_ammo_photos')

        # Deleting model 'AmmoCaliber'
        db.delete_table(u'base_ammocaliber')


    models = {
        u'base.ammo': {
            'Meta': {'unique_together': "(('name', 'head_stamp', 'year', 'ammo_type', 'primer_varnish_color', 'total_weight', 'percussion_type', 'projectile_diameter', 'projectile_weight', 'projectile_material', 'serrated', 'has_magnetic_properties', 'projectile_varnish_color', 'tip_color', 'tip_type', 'tip_shape', 'gunpowder_type', 'gunpowder_weight', 'gunpowder_color', 'casing_weight', 'casing_type', 'casing_material', 'casing_length'),)", 'object_name': 'Ammo'},
            'ammo_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'casing_length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'casing_material': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'casing_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'casing_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Country']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'factory': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'gunpowder_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'gunpowder_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'gunpowder_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'has_magnetic_properties': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'head_stamp': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'percussion_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photologue.Photo']", 'symmetrical': 'False'}),
            'primer_varnish_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'projectile_diameter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'projectile_material': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'projectile_varnish_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'projectile_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'serrated': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'blank': 'True'}),
            'tip_color': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'tip_shape': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'tip_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'total_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'base.ammocaliber': {
            'Meta': {'unique_together': "(('ammo', 'caliber_type', 'caliber_value'),)", 'object_name': 'AmmoCaliber'},
            'ammo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'calibers'", 'to': u"orm['base.Ammo']"}),
            'caliber_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'caliber_value': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.country': {
            'Meta': {'object_name': 'Country'},
            'country_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'country_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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