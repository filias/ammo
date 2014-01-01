from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from base.models import Ammo, AmmoCasing, AmmoGunpowder, \
    AmmoCaliber, AmmoProjectile


class PhotoInline(admin.TabularInline):
    model = Ammo.photos.through


class AmmoCaliberInline(admin.StackedInline):
    model = AmmoCaliber
    extra = 4
    max_num = 4
    exclude = ('caliber_type',)


class AmmoCasingAdmin(admin.ModelAdmin):

    class Meta:
        model = AmmoCasing


class AmmoGunpowderAdmin(admin.ModelAdmin):

    class Meta:
        model = AmmoGunpowder


class AmmoProjectileAdmin(admin.ModelAdmin):

    class Meta:
        model = AmmoProjectile


class AmmoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'head_stamp', 'year', 'ammo_type',
            'primer_varnish_color', 'total_weight',
            'percussion_type', 'country', 'factory')
        }),
        (_('Details'), {
            'fields': ('casing', 'gunpowder', 'projectile'),
        }),
        (_('Other'), {
            'fields': ('notes', )
        }),
    )
    list_display = ('name', 'year', 'country', 'projectile', 'casing',
                    'gunpowder')
    list_filter = ('country', 'ammo_type', 'projectile', 'casing',
                   'gunpowder', 'head_stamp')
    search_fields = ['name', 'year']
    inlines = [AmmoCaliberInline, PhotoInline]
    exclude = ('photos', )

    class Meta:
        model = Ammo

admin.site.register(Ammo, AmmoAdmin)
admin.site.register(AmmoCasing, AmmoCasingAdmin)
admin.site.register(AmmoGunpowder, AmmoGunpowderAdmin)
admin.site.register(AmmoProjectile, AmmoProjectileAdmin)

# Unregister default models
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
admin.site.unregister(Site)
admin.site.unregister(Group)
