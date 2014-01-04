#-*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from photologue.models import Photo

from base.choices import *


class Ammo(models.Model):
    name = models.CharField(_('name'), max_length=64)  # calibre
    head_stamp = models.CharField(_('head stamp'), max_length=64, blank=True)  # headstamp
    year = models.CharField(_('year'), max_length=4, choices=YEAR_CHOICES, blank=True)  # ano de fabrico
    ammo_type = models.CharField(_('ammo type'), max_length=32, choices=AMMO_TYPE_CHOICES, blank=True)  # tipo
    primer_varnish_color = models.CharField(_('primer varnish color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor do verniz parte f
    total_weight = models.FloatField(_('total weight'), null=True, blank=True, help_text=_('(in grams)'))  # peso total
    percussion_type = models.CharField(_('percussion type'), max_length=32, choices=PERCUSSION_TYPE_CHOICES, blank=True)  # tipo de percussao

    country = models.CharField(_('country'), max_length=2, choices=COUNTRY_CHOICES, blank=True)  # pais
    factory = models.CharField(_('factory'), max_length=128, blank=True)  # fabrica
    notes = models.TextField(_('notes'), blank=True)  # notas

    # Projectile
    projectile_diameter = models.FloatField(_('projectile diameter'), null=True, blank=True, help_text=_('(in mm)'))  # B0
    projectile_weight = models.FloatField(_('projectile weight'), null=True, blank=True, help_text=_('(in grams)'))  # peso do projectil pode variar
    projectile_material = models.CharField(_('projectile material'), max_length=32, choices=PROJECTILE_MATERIAL_CHOICES, blank=True)  # material do projectil
    serrated = models.CharField(_('serrated'), max_length=1, choices=PROJECTILE_SS_CHOICES, blank=True, default='0')  # sulco serrilhado
    has_magnetic_properties = models.BooleanField(_('magnetic properties'), default=False)  # propriedades magneticas
    projectile_varnish_color = models.CharField(_('projectile varnish color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor do verniz parte p
    tip_color = models.CharField(_('tip color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor da ponta
    tip_type = models.CharField(_('tip type'), max_length=32, choices=TIP_TYPE_CHOICES, blank=True)  # tipo de ponta
    tip_shape = models.CharField(_('tip shape'), max_length=32, choices=TIP_SHAPE_CHOICES, blank=True)  # forma da ponta

    # Gunpowder
    gunpowder_type = models.CharField(_('gunpowder type'), max_length=32, choices=GUNPOWDER_TYPE_CHOICES, blank=True)  # tipo de polvora
    gunpowder_color = models.CharField(_('gunpowder color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor da polvora
    gunpowder_weight = models.FloatField(_('gunpowder weight'), null=True, blank=True, help_text=_('(in grams)'))  # peso da polvora

    # Casing
    casing_weight = models.FloatField(_('casing weight'), blank=True, null=True, help_text=_('in grams'))  # peso do involucro
    casing_type = models.CharField(_('casing type'), max_length=32, choices=CASING_TYPE_CHOICES, blank=True)  # tipo do involucro
    casing_material = models.CharField(_('casing material'), max_length=32, choices=CASING_MATERIAL_CHOICES, blank=True)  # material do involucro
    casing_length = models.FloatField(_('casing length'), blank=True, null=True, help_text=_('(in mm)'))  # cl

    # Photos
    photos = models.ManyToManyField(Photo, verbose_name=_('photos'))

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @property
    def projectile_display(self):
        result = ''
        result += self.get_tip_type_display() + ' ' if self.get_tip_type_display() else ''
        result += self.get_tip_shape_display() + ' ' if self.get_tip_shape_display() else ''
        result += self.get_tip_color_display() if self.get_tip_color_display() else ''
        return result

    class Meta:
        unique_together = ('name',
                           'head_stamp',
                           'year',
                           'ammo_type',
                           'primer_varnish_color',
                           'total_weight',
                           'percussion_type',
                           'projectile_diameter',
                           'projectile_weight',
                           'projectile_material',
                           'serrated',
                           'has_magnetic_properties',
                           'projectile_varnish_color',
                           'tip_color',
                           'tip_type',
                           'tip_shape',
                           'gunpowder_type',
                           'gunpowder_weight',
                           'gunpowder_color',
                           'casing_weight',
                           'casing_type',
                           'casing_material',
                           'casing_length')
        verbose_name = _('Ammunition')
        verbose_name_plural = _('Ammunitions')


class AmmoCaliber(models.Model):
    ammo = models.ForeignKey(Ammo, related_name='calibers')
    caliber_type = models.CharField(_('caliber type'), max_length=2, choices=CALIBER_TYPE_CHOICES, blank=True)
    caliber_value = models.CharField(_('caliber value'), max_length=32, blank=True)

    class Meta:
        unique_together = ('ammo', 'caliber_type', 'caliber_value')
        verbose_name = _('Caliber')
        verbose_name_plural = _('Calibers')
