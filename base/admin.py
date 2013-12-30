from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from base.models import Ammo, AmmoCover, AmmoGunpowder, \
    AmmoCaliber, AmmoProjectile, AmmoTip


class PhotoInline(admin.TabularInline):
    model = Ammo.photos.through


class AmmoCaliberInline(admin.StackedInline):
    model = AmmoCaliber
    extra = 4


class AmmoCoverAdmin(admin.ModelAdmin):

    class Meta:
        model = AmmoCover


class AmmoGunpowderAdmin(admin.ModelAdmin):

    class Meta:
        model = AmmoGunpowder


class AmmoProjectileAdmin(admin.ModelAdmin):

    class Meta:
        model = AmmoProjectile


class AmmoTipAdmin(admin.ModelAdmin):

    class Meta:
        model = AmmoTip


class AmmoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'head_stamp', 'year', 'ammo_type',
            'fulminant_varnish_color', 'total_weight',
            'percussion_type', 'country', 'factory')
        }),
        (_('Details'), {
            'fields': ('cover', 'gunpowder', 'projectile', 'tip'),
        }),
        (_('Other'), {
            'fields': ('notes', )
        }),
    )
    list_filter = ('head_stamp', 'ammo_type')
    search_fields = ['year']
    inlines = [AmmoCaliberInline, PhotoInline]
    exclude = ('photos', )

    class Meta:
        model = Ammo

admin.site.register(Ammo, AmmoAdmin)
admin.site.register(AmmoCover, AmmoCoverAdmin)
admin.site.register(AmmoGunpowder, AmmoGunpowderAdmin)
admin.site.register(AmmoProjectile, AmmoProjectileAdmin)
admin.site.register(AmmoTip, AmmoTipAdmin)

# Unregister default models
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
admin.site.unregister(Site)
admin.site.unregister(Group)
