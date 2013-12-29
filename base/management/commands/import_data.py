import csv

from django.core.management import BaseCommand


class Command(BaseCommand):
    """Reads the csv file and puts it in the db"""

    def handle(self, *args, **options):
        pass