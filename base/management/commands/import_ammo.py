import csv
import os

from django.core.management import BaseCommand

from base.models import Ammo, AmmoCaliber, AmmoCover, AmmoGunpowder, \
    AmmoProjectile, AmmoTip


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
          'cinza': 'ga'}

def fix_color(color, part=None):
    if not color:
        return ''

    color = color.lower()
    if part == 'f':
        # cor do verniz do fulminante
        color = color.replace('f-', '')
    elif part == 'p':
        # cor do verniz do projectil
        color = color.replace('p-', '')

    if color in COLORS:
        return COLORS[color]
    else:
        print 'color not in dict ' + color
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
        kwargs_ammo['fulminant_varnish_color'] = fix_color(line[4].strip(), part='f')
        kwargs_ammo['country'] = line[10].strip()
        kwargs_ammo['factory'] = line[11].strip()
        kwargs_ammo['total_weight'] = fix_float(line[16].strip())
        kwargs_ammo['percussion_type'] = line[27].strip()
        kwargs_ammo['notes'] = line[28].strip()

        # Caliber
        kwargs_calibers = dict()
        kwargs_calibers['caliber_1'] = line[12].strip()
        kwargs_calibers['caliber_2'] = line[13].strip()
        kwargs_calibers['caliber_3'] = line[14].strip()
        kwargs_calibers['caliber_4'] = line[15].strip()

        # Tip
        kwargs_tip = dict()
        kwargs_tip['tip_color'] = fix_color(line[5].strip())
        kwargs_tip['tip_type'] = line[6].strip()
        kwargs_tip['tip_shape'] = line[7].strip()

        # Projectile
        kwargs_projectile = dict()
        kwargs_projectile['projectile_diameter'] = fix_float(line[8].strip())
        kwargs_projectile['projectile_material'] = line[19].strip()
        kwargs_projectile['projectile_weight'] = fix_float(line[21].strip())
        kwargs_projectile['has_magnetic_properties'] = line[18].strip() == 'Sim'
        kwargs_projectile['sulco_serrilhado'] = line[20].strip()
        kwargs_projectile['projectile_varnish_color'] = fix_color(line[4].strip(), part='p')

        # Cover
        kwargs_cover = dict()
        kwargs_cover['cover_length'] = fix_float(line[9].strip())
        kwargs_cover['cover_material'] = line[22].strip()
        kwargs_cover['cover_type'] = line[23].strip()
        kwargs_cover['cover_weight'] = fix_float(line[24].strip())

        # Gunpowder
        kwargs_gunpowder = dict()
        kwargs_gunpowder['gunpowder_type'] = line[25].strip()
        kwargs_gunpowder['gunpowder_color'] = fix_color(line[26].strip())
        kwargs_gunpowder['gunpowder_weight'] = fix_float(line[17].strip())

        # Put together
        for key in ('ammo', 'tip', 'cover', 'calibers', 'projectile', 'gunpowder'):
            result[key] = locals()['kwargs_' + key]

        return result

    def create_ammocover(self, **kwargs):
        cover, created = AmmoCover.objects.get_or_create(**kwargs)
        return cover

    def create_ammoprojectile(self, **kwargs):
        projectile, created = AmmoProjectile.objects.get_or_create(**kwargs)
        return projectile

    def create_ammogunpowder(self, **kwargs):
        gunpowder, created = AmmoGunpowder.objects.get_or_create(**kwargs)
        return gunpowder

    def create_ammotip(self, **kwargs):
        tip, created = AmmoTip.objects.get_or_create(**kwargs)
        return tip

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
                for key in ('cover', 'projectile', 'gunpowder', 'tip'):
                    values[key] = getattr(self, 'create_ammo' + key)(**result[key])

                # Create calibers
                # TODO

                # Create ammo
                ammo = Ammo.objects.create(**result['ammo'])
                for key in ('cover', 'projectile', 'gunpowder', 'tip'):
                    ammo.key = values[key]
