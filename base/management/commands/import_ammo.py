#-*- coding: UTF-8 -*-
import csv
import os

from django.core.management import BaseCommand
from unidecode import unidecode

from base.models import Ammo, AmmoCaliber, Country
from base.choices import COUNTRY_CHOICES


def fix_float(value):
    if not value:
        return None

    if ',' in value:
        value = value.replace(',', '.')

    for end in ('g', 'mm'):
        if value.endswith(end):
            value = value.replace(end, '')

    return float(value)


COLORS = {'vermelho': 're',
          'vermelha': 're',
          'verde': 'gr',
          'verde-escuro': 'dg',
          'preto': 'bl',
          'preta': 'bl',
          'branco': 'wh',
          'branca': 'wh',
          'azul': 'bl',
          'azul escuro': 'db',
          'prata': 'si',
          'roxo': 'pu',
          'roxa': 'pu',
          'laranja': 'or',
          'castanho': 'br',
          'cinza': 'ga'}

def fix_color(color):
    if not color:
        return ''

    color = color.lower()
    if color in COLORS:
        return COLORS[color]
    else:
        print 'color not in dict ' + color
        return ''


COUNTRIES = {
    'belgica': 'be',
    'bulgaria': 'bu',
    'suica': 'ch',
    'china': 'ci',
    'checoslovaquia': 'cs',
    'alemanha': 'de',
    'finlandia': 'fi',
    'franca': 'fr',
    'italia': 'it',
    'polonia': 'pl',
    'inglaterra': 'uk',
    'urss': 'ur',
    'usa': 'us',
    'yugoslavia': 'yu',
}

def create_countries():
    for it in COUNTRY_CHOICES:
        Country.objects.create(country_name=it[1], country_code=it[0])


def fix_country(country):
    if not country:
        return None

    country = unidecode(unicode(country.lower()))
    if country in COUNTRIES:
        code = COUNTRIES[country]
        return Country.objects.get(country_code=code)
    else:
        print 'country not in dict ' + country
        return None


def create_slug(value):
    if not value:
        return ''

    try:
        value = unidecode(unicode(value.lower().replace(' ', '-')))
    except UnicodeDecodeError:
        import ipdb; ipdb.set_trace()
    return value


class Command(BaseCommand):
    """Reads the csv file and puts it in the db"""

    def get_values(self, line):
        result = dict()

        # Ammo
        kwargs_ammo = dict()
        kwargs_ammo['name'] = unicode(line[0].strip())
        kwargs_ammo['head_stamp'] = unicode(line[1].strip())
        kwargs_ammo['year'] = line[2].strip()
        kwargs_ammo['ammo_type'] = create_slug(line[3].strip())
        kwargs_ammo['primer_varnish_color'] = fix_color(line[4].strip())
        kwargs_ammo['country'] = fix_country(line[11].strip())
        kwargs_ammo['factory'] = unicode(line[12].strip())
        kwargs_ammo['total_weight'] = fix_float(line[17].strip())
        kwargs_ammo['percussion_type'] = create_slug(line[28].strip())
        kwargs_ammo['notes'] = unicode(line[29].strip())

        # Caliber
        kwargs_calibers = dict()
        kwargs_calibers['a1'] = unicode(line[13].strip())
        kwargs_calibers['a2'] = unicode(line[14].strip())
        kwargs_calibers['a3'] = unicode(line[15].strip())
        kwargs_calibers['a4'] = unicode(line[16].strip())

        # Projectile
        kwargs_ammo['projectile_diameter'] = fix_float(line[9].strip())
        kwargs_ammo['projectile_material'] = create_slug(line[20].strip())
        kwargs_ammo['projectile_weight'] = fix_float(line[18].strip())
        kwargs_ammo['has_magnetic_properties'] = unicode(line[19].strip()) == 'Sim'
        kwargs_ammo['serrated'] = 1 if unicode(line[21].strip()) == 'Sim' else 1
        kwargs_ammo['projectile_varnish_color'] = fix_color(line[5].strip())
        kwargs_ammo['tip_color'] = fix_color(line[6].strip())
        kwargs_ammo['tip_type'] = create_slug(line[7].strip())
        kwargs_ammo['tip_shape'] = create_slug(line[8].strip())

        # Casing
        kwargs_ammo['casing_length'] = fix_float(line[10].strip())
        kwargs_ammo['casing_material'] = create_slug(line[23].strip())
        kwargs_ammo['casing_type'] = create_slug(line[24].strip())
        kwargs_ammo['casing_weight'] = fix_float(line[25].strip())

        # Gunpowder
        kwargs_ammo['gunpowder_type'] = create_slug(line[26].strip())
        kwargs_ammo['gunpowder_color'] = fix_color(line[27].strip())
        kwargs_ammo['gunpowder_weight'] = fix_float(line[22].strip())

        # Put together
        for key in ('ammo', 'calibers'):
            result[key] = locals()['kwargs_' + key]

        return result

    def create_ammocaliber(self, ammo, **kwargs):
        for key, value in kwargs.items():
            AmmoCaliber.objects.get_or_create(ammo=ammo,
                                              caliber_type=key,
                                              caliber_value=value)

    def handle(self, *args, **options):

        create_countries()

        filename = 'ammo-lagoa.csv'
        filepath = os.path.join(os.path.curdir, 'db', filename)

        with open(filepath) as f:
            csv_reader = csv.reader(f, delimiter='\t')

            for idx, line in enumerate(csv_reader):
                if idx in (0, 1):
                    continue
                # Save values
                result = self.get_values(line)

                # Create ammo
                ammo = Ammo.objects.create(**result['ammo'])
                print 'created ammo {}'.format(ammo.pk)

                # Create calibers
                self.create_ammocaliber(ammo, **result['calibers'])
                print 'created calibers for ammo {}'.format(ammo.pk)