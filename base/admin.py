from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from base.models import Ammo, AmmoCaliber, Country


class PhotoInline(admin.TabularInline):
    model = Ammo.photos.through


class AmmoCaliberInline(admin.StackedInline):
    model = AmmoCaliber
    extra = 4
    max_num = 4
    exclude = ('caliber_type',)


class AmmoAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('General'),
         {'fields': ('name', 'head_stamp', 'year', 'ammo_type',
                     'primer_varnish_color', 'total_weight',
                     'percussion_type', 'country', 'factory')}),

        (_('Projectile'),
         {'fields': ('projectile_diameter', 'projectile_weight',
                     'projectile_material', 'serrated',
                     'has_magnetic_properties', 'projectile_varnish_color',
                     'tip_color', 'tip_type', 'tip_shape')}),

        (_('Casing'),
         {'fields': ('casing_weight', 'casing_type',
                     'casing_material', 'casing_length')}),

        (_('Gunpowder'),
         {'fields': ('gunpowder_type', 'gunpowder_color', 'gunpowder_weight')}),

        (_('Other'), {
            'fields': ('notes', )
        }),
    )

    list_display = ('name', 'head_stamp', 'projectile_display', 'year', 'country',
                    'has_magnetic_properties')

    list_filter = ('country', 'ammo_type', 'name', 'head_stamp')

    search_fields = ['name', 'year']

    inlines = [AmmoCaliberInline, PhotoInline]
    exclude = ('photos', )

    class Meta:
        model = Ammo


class CountryAdmin(admin.ModelAdmin):

    class Meta:
        model = Country

admin.site.register(Ammo, AmmoAdmin)
admin.site.register(Country, CountryAdmin)

# Unregister default models
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
admin.site.unregister(Site)
admin.site.unregister(Group)
