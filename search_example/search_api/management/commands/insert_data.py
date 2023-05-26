import csv

from django.core.management.base import BaseCommand, CommandError

from search_api.models import Candidate


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            _ = next(dataReader)
            for row in dataReader:
                _, created = Candidate.objects.get_or_create(
                    score=row[0],
                    name=row[1],
                    skill=row[2])
