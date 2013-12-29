import csv
import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    """Reads the csv file and puts it in the db"""

    def get_values(self, line):
        result = dict()
        result['caliber'] = line[0]
        result['head_stamp'] = line[1]
        result['year'] = line[2]
        result['ammo_type'] = line[3]
        result['varnish_color'] = line[4]
        result['tip_color'] = line[5]
        result['tip_type'] = line[6]
        result['tip_shape'] = line[7]
        result['projectile_diameter'] = line[8]
        result['cover_length'] = line[9]
        result['country'] = line[10]
        result['factory'] = line[11]
        result['caliber_1'] = line[12]
        result['caliber_2'] = line[13]
        result['caliber_3'] = line[14]
        result['caliber_4'] = line[15]
        result['total_weight'] = line[16]
        result['weight'] = line[17]
        result['has_magnetic_properties'] = line[18]
        result['projectile_material'] = line[19]
        result['sulco_serrilhado'] = line[20]
        result['projectile_weight'] = line[21]
        result['cover_material'] = line[22]
        result['cover_type'] = line[23]
        result['cover_weight'] = line[24]
        result['gunpowder_type'] = line[25]
        result['gunpowder_color'] = line[26]
        result['percussion_type'] = line[27]
        result['notes'] = line[28]
        return result

    def handle(self, *args, **options):

        # Get the values
        filename = 'ammo-lagoa.csv'
        filepath = os.path.join(os.path.curdir, 'db', filename)

        with open(filepath) as f:
            csv_reader = csv.reader(f, delimiter='\t')

            for line in csv_reader:
                # Save values
                values = self.get_values(line)

                print values['ammo_type']
                # Create ammocover

                # Create the dependencies