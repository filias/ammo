#-*- coding: UTF-8 -*-
import csv
import os

from django.core.management import BaseCommand

from base.models import Ammo, AmmoCaliber, AmmoCasing, AmmoGunpowder, \
    AmmoProjectile


AMMO_PARTS = ('casing', 'projectile', 'gunpowder')

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


TIP_TYPES = {
    'chumbo': 'pb',
    'teflon': 'tf',
    'fmj': 'fm',
    'round nose': 'rn',
    'hollow point': 'hp',
    'hidra shock': 'hs',
    'madeira': 'wo',
    'borracha': 'ru',
    'cromada': 'cr',
}

def fix_tip_type(tip_type):
    if not tip_type:
        return ''

    tip_type = tip_type.lower()
    if tip_type in TIP_TYPES:
        return TIP_TYPES[tip_type]
    else:
        print 'tip type not in dict ' + tip_type
        return ''

TIP_SHAPES = {
    'hollow cavity': 'hc',
    'hollow point': 'hp',
    'round nose': 'rn',
    'flat point': 'fp',
    'truncated': 'tr',
    'semi-wadcute': 'sw',
    'calepino de papel': 'cp',
    'spitzer': 'sp',
    'boat-tail': 'bt',
}

def fix_tip_shape(tip_shape):
    if not tip_shape:
        return ''

    tip_shape = tip_shape.lower()
    if tip_shape in TIP_SHAPES:
        return TIP_SHAPES[tip_shape]
    else:
        print 'tip shape not in dict ' + tip_shape
        return ''


class Command(BaseCommand):
    """Reads the csv file and puts it in the db"""

    def get_values(self, line):
        result = dict()

        # Ammo
        kwargs_ammo = dict()
        kwargs_ammo['name'] = line[0].strip()
        kwargs_ammo['head_stamp'] = line[1].strip()
        kwargs_ammo['year'] = line[2].strip()
        kwargs_ammo['ammo_type'] = line[3].strip()
        kwargs_ammo['primer_varnish_color'] = fix_color(line[4].strip())
        kwargs_ammo['country'] = line[11].strip()
        kwargs_ammo['factory'] = line[12].strip()
        kwargs_ammo['total_weight'] = fix_float(line[17].strip())
        kwargs_ammo['percussion_type'] = line[28].strip()
        kwargs_ammo['notes'] = line[29].strip()

        # Caliber
        kwargs_calibers = dict()
        kwargs_calibers['caliber_1'] = line[13].strip()
        kwargs_calibers['caliber_2'] = line[14].strip()
        kwargs_calibers['caliber_3'] = line[15].strip()
        kwargs_calibers['caliber_4'] = line[16].strip()

        # Projectile
        kwargs_projectile = dict()
        kwargs_projectile['projectile_diameter'] = fix_float(line[9].strip())
        kwargs_projectile['projectile_material'] = line[20].strip()
        kwargs_projectile['projectile_weight'] = fix_float(line[18].strip())
        kwargs_projectile['has_magnetic_properties'] = line[19].strip() == 'Sim'
        kwargs_projectile['serrated'] = line[21].strip()
        kwargs_projectile['projectile_varnish_color'] = fix_color(line[5].strip())
        kwargs_projectile['tip_color'] = fix_color(line[6].strip())
        kwargs_projectile['tip_type'] = fix_tip_type(line[7].strip())
        kwargs_projectile['tip_shape'] = fix_tip_shape(line[8].strip())

        # Casing
        kwargs_casing = dict()
        kwargs_casing['casing_length'] = fix_float(line[10].strip())
        kwargs_casing['casing_material'] = line[23].strip()
        kwargs_casing['casing_type'] = line[24].strip()
        kwargs_casing['casing_weight'] = fix_float(line[25].strip())

        # Gunpowder
        kwargs_gunpowder = dict()
        kwargs_gunpowder['gunpowder_type'] = line[26].strip()
        kwargs_gunpowder['gunpowder_color'] = fix_color(line[27].strip())
        kwargs_gunpowder['gunpowder_weight'] = fix_float(line[22].strip())

        # Put together
        for key in ('ammo', 'casing', 'calibers', 'projectile', 'gunpowder'):
            result[key] = locals()['kwargs_' + key]

        return result

    def create_ammocover(self, **kwargs):
        cover, created = AmmoCasing.objects.get_or_create(**kwargs)
        return cover

    def create_ammoprojectile(self, **kwargs):
        projectile, created = AmmoProjectile.objects.get_or_create(**kwargs)
        return projectile

    def create_ammogunpowder(self, **kwargs):
        gunpowder, created = AmmoGunpowder.objects.get_or_create(**kwargs)
        return gunpowder

    def handle(self, *args, **options):
        filename = 'ammo-lagoa.csv'
        filepath = os.path.join(os.path.curdir, 'db', filename)

        with open(filepath) as f:
            csv_reader = csv.reader(f, delimiter='\t')

            for idx, line in enumerate(csv_reader):
                if idx == 0:
                    continue
                # Save values
                result = self.get_values(line)

                # Create dependencies
                values = dict()
                for key in AMMO_PARTS:
                    values[key] = getattr(self, 'create_ammo' + key)(**result[key])

                # Create calibers
                # TODO

                # Create ammo
                ammo = Ammo.objects.create(**result['ammo'])
                for key in AMMO_PARTS:
                    ammo.key = values[key]
