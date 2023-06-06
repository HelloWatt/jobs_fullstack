from django.core import serializers
from django.core.management.base import BaseCommand

from admintools.generators.generate_prices import generate_prices
from dashboard.models import ElectricityPrice


class Command(BaseCommand):
    help = "Generate fixtures for consumptions"

    def add_arguments(self, parser):
        parser.add_argument(
            "fixturepath",
            help="A file where the prices fixture will be saved",
            nargs="?",
            default="./dashboard/fixtures/prices.json",
        )

    def handle(self, *args, **options):
        ElectricityPrice.objects.all().delete()
        generate_prices()
        fixtures = serializers.serialize(
            "json", ElectricityPrice.objects.all(), indent=2
        )
        with open(options["fixturepath"], "w") as f:
            f.write(fixtures)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully saved fixture to {options['fixturepath']}"
                )
            )
