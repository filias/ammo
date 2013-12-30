import datetime

from django.utils.translation import ugettext_lazy as _


COLOR_CHOICES = (
    ('re', _('Red')),
    ('gr', _('Green')),
    ('dg', _('Dark Green')),
    ('bl', _('Black')),
    ('wh', _('White')),
    ('bl', _('Blue')),
    ('db', _('Dark Blue')),
    ('ga', _('Gray')),
    ('pu', _('Purple')),
    ('br', _('Brown')),
    ('or', _('Orange')),
    ('si', _('Silver')),
)

TIP_TYPE_CHOICES = (
    ('pb', _('Plumb')),
    ('tf', _('Teflon')),
    ('fm', _('FMJ')),
)

TIP_SHAPE_CHOICES = (
    ('hc', _('Hollow cavity')),
    ('hp', _('Hollow point')),
    ('rn', _('Round nose')),
    ('fp', _('Flat point')),
)

CALIBER_TYPE_CHOICES = (
    ('a1', _('alternative caliber 1')),
    ('a2', _('alternative caliber 2')),
    ('a3', _('alternative caliber 3')),
    ('a4', _('alternative caliber 4')),
)

COVER_TYPE_CHOICES = (
    ('ri', _('rimmed')),
    ('rl', _('rimless')),
)

COVER_MATERIAL_CHOICES = (
    ('lt', _('latao')),
    ('al', _('aluminio')),
)

GUNPOWDER_TYPE_CHOICES = (
    ('pl', _('polvora laminada')),
    ('pd', _('polvora em discos')),
    ('pe', _('polvora esferica')),
)

YEAR_CHOICES = (
    ('%s' % i, i) for i in range(1700, datetime.date.today().year + 1)
)

AMMO_TYPE_CHOICES = (
    ('ex', _('exercicio')),
    ('ss', _('shotshell')),
    ('re', _('real')),
    ('rt', _('real tracejante')),
    ('rc', _('real prateada')),
    ('rp', _('real cobreada')),
    ('ri', _('real incendiaria')),
    ('sa', _('salva')),
)

COUNTRY_CHOICES = (
    ('be', _('Belgium')),
    ('bu', _('Bulgaria')),
    ('ch', _('Switzerland')),
    ('ci', _('China')),
    ('cs', _('Checoslovakia')),
    ('de', _('Germany')),
    ('fi', _('Finland')),
    ('fr', _('France')),
    ('pl', _('Poland')),
    ('uk', _('UK')),
    ('ur', _('USSR')),
    ('us', _('USA')),
    ('yu', _('Yugoslavia')),
)

PERCUSSION_TYPE_CHOICES = (
    ('an', _('anelar')),
    ('ce', _('central')),
)

PROJECTILE_SS_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

PROJECTILE_MATERIAL_CHOICES = (
    ('ch', _('chumbo')),
    ('cc', _('chumbo cobreado')),
    ('cd', _('chumbo dourado')),
    ('co', _('chumbo com camisa de cobre')),
    ('ca', _('chumbo com camisa de cobre e aco')),
)

