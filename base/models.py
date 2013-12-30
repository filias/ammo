from django.db import models
from django.utils.translation import ugettext_lazy as _

from photologue.models import Photo

from base.choices import *


class AmmoCover(models.Model):
    cover_weight = models.FloatField(_('cover weight'), blank=True, null=True, help_text=_('in grams'))  # peso do involucro
    cover_type = models.CharField(_('cover type'), max_length=2, choices=COVER_TYPE_CHOICES, blank=True)  # tipo do involucro
    cover_material = models.CharField(_('cover material'), max_length=2, choices=COVER_MATERIAL_CHOICES, blank=True)  # material do involucro
    cover_length = models.FloatField(_('cover length'), blank=True, null=True, help_text=_('(in mm)'))  # cl

    def __unicode__(self):
        return '{} {} {}mm {}g'.format(self.get_cover_material_display(),
                                       self.get_cover_type_display(),
                                       self.cover_length,
                                       self.cover_weight)

    class Meta:
        unique_together = ('cover_weight', 'cover_type', 'cover_material', 'cover_length')
        verbose_name = _('Cover')
        verbose_name_plural = _('Covers')


class AmmoGunpowder(models.Model):
    gunpowder_type = models.CharField(_('gunpowder type'), max_length=2, choices=GUNPOWDER_TYPE_CHOICES, blank=True)  # tipo de polvora
    gunpowder_color = models.CharField(_('gunpowder color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor da polvora
    gunpowder_weight = models.FloatField(_('gunpowder weight'), null=True, blank=True, help_text=_('(in grams)'))  # peso da polvora

    def __unicode__(self):
        return '{} {}'.format(self.get_gunpowder_type_display(),
                              self.get_gunpowder_color_display())

    class Meta:
        unique_together = ('gunpowder_type', 'gunpowder_weight', 'gunpowder_color')
        verbose_name = _('Gunpowder')
        verbose_name_plural = _('Gunpowder')


class AmmoProjectile(models.Model):
    projectile_diameter = models.FloatField(_('projectile diameter'), null=True, blank=True, help_text=_('(in mm)'))  # B0
    projectile_weight = models.FloatField(_('projectile weight'), null=True, blank=True, help_text=_('(in grams)'))  # peso do projectil pode variar
    projectile_material = models.CharField(_('projectile material'), max_length=2, choices=PROJECTILE_MATERIAL_CHOICES, blank=True)  # material do projectil
    sulco_serrilhado = models.CharField(_('sulco serrilhado'), max_length=1, choices=PROJECTILE_SS_CHOICES, blank=True, default='0')  # sulco serrilhado
    has_magnetic_properties = models.BooleanField(_('magnetic properties'), default=False)  # propriedades magneticas
    projectile_varnish_color = models.CharField(_('projectile varnish color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor do verniz parte p

    def __unicode__(self):
        return '{} {}mm {}g {} {}'.format(self.get_projectile_material_display(),
                                          self.projectile_diameter,
                                          self.projectile_weight,
                                          self.has_magnetic_properties,
                                          self.get_sulco_serrilhado_display())

    class Meta:
        unique_together = ('projectile_diameter', 'projectile_weight',
                           'projectile_material', 'sulco_serrilhado',
                           'has_magnetic_properties', 'projectile_varnish_color')
        verbose_name = _('Projectile')
        verbose_name_plural = _('Projectiles')


class AmmoTip(models.Model):
    tip_color = models.CharField(_('tip color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor da ponta
    tip_type = models.CharField(_('tip type'), max_length=2, choices=TIP_TYPE_CHOICES, blank=True)  # tipo de ponta
    tip_shape = models.CharField(_('tip shape'), max_length=2, choices=TIP_SHAPE_CHOICES, blank=True)  # forma da ponta

    def __unicode__(self):
        return '{} {} {}'.format(self.get_tip_type_display(),
                                 self.get_tip_color_display(),
                                 self.get_tip_shape_display())

    class Meta:
        unique_together = ('tip_color', 'tip_type', 'tip_shape')
        verbose_name = _('Tip')
        verbose_name_plural = _('Tips')


class Ammo(models.Model):
    name = models.CharField(_('name'), max_length=64)  # calibre
    head_stamp = models.TextField(_('head stamp'), blank=True)  # headstamp
    year = models.CharField(_('year'), max_length=4, choices=YEAR_CHOICES, blank=True)  # ano de fabrico
    ammo_type = models.CharField(_('ammo type'), max_length=2, choices=AMMO_TYPE_CHOICES, blank=True)  # tipo
    fulminant_varnish_color = models.CharField(_('fulminant varnish color'), max_length=2, choices=COLOR_CHOICES, blank=True)  # cor do verniz parte f
    total_weight = models.FloatField(_('total weight'), null=True, blank=True, help_text=_('(in grams)'))  # peso total
    percussion_type = models.CharField(_('percussion type'), max_length=2, choices=PERCUSSION_TYPE_CHOICES, blank=True)  # tipo de percussao

    country = models.CharField(_('country'), max_length=2, choices=COUNTRY_CHOICES, blank=True)  # pais
    factory = models.CharField(_('factory'), max_length=128, blank=True)  # fabrica
    notes = models.TextField(_('notes'), blank=True)  # notas

    # Foreign keys
    tip = models.ForeignKey(AmmoTip, blank=True, null=True, verbose_name=_('tip'))
    projectile = models.ForeignKey(AmmoProjectile, blank=True, null=True, verbose_name=_('projectile'))
    cover = models.ForeignKey(AmmoCover, blank=True, null=True, verbose_name=_('cover'))
    gunpowder = models.ForeignKey(AmmoGunpowder, blank=True, null=True, verbose_name=_('gunpowder'))
    photos = models.ManyToManyField(Photo, verbose_name=_('photos'))

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Ammunition')
        verbose_name_plural = _('Ammunitions')


class AmmoCaliber(models.Model):
    ammo = models.ForeignKey(Ammo, related_name='calibers')
    caliber_type = models.CharField(_('caliber type'), max_length=2, choices=CALIBER_TYPE_CHOICES, blank=True)
    caliber_value = models.CharField(_('caliber value'), max_length=32, blank=True)

    class Meta:
        unique_together = ('caliber_type', 'caliber_value')
        verbose_name = _('Caliber')
        verbose_name_plural = _('Calibers')
