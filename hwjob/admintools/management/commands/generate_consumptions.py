import random

from django.core import serializers
from django.core.management.base import BaseCommand
import json

from admintools.generators.generate_consumptions import generate_consumptions


class Command(BaseCommand):
    help = "Generate fixtures for consumptions"

    def add_arguments(self, parser):
        parser.add_argument(
            "nb_clients",
            help="The number of clients to generate",
            nargs="?",
            default=100,
            type=int,
        )
        parser.add_argument(
            "consofixturepath",
            help="A file where the consumptions fixture will be saved",
            nargs="?",
            default="./dashboard/fixtures/consumptions.json",
        )
        parser.add_argument(
            "clientfixturepath",
            help="A file where the clients fixture will be saved",
            nargs="?",
            default="./dashboard/fixtures/clients.json",
        )
        parser.add_argument(
            "metadataspath",
            help="A file where the metadatas will be saved",
            nargs="?",
            default="./dashboard/metadata/consumptions.json",
        )

    def handle(self, *args, **options):
        consumptions, cients, metadatas = generate_consumptions(options["nb_clients"])
        random.shuffle(consumptions)
        self.show_stats(metadatas)
        conso_fixtures = serializers.serialize("json", consumptions, indent=2)
        with open(options["consofixturepath"], "w") as f:
            f.write(conso_fixtures)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully saved fixture to {options['consofixturepath']}"
                )
            )
        client_fixtures = serializers.serialize("json", cients, indent=2)
        with open(options["clientfixturepath"], "w") as f:
            f.write(client_fixtures)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully saved fixture to {options['clientfixturepath']}"
                )
            )
        with open(options["metadataspath"], "w") as f:
            json.dump(metadatas, f, indent=2)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully saved metadatas to {options['metadataspath']}"
                )
            )

    def show_stats(self, metadatas):
        elec_heating_count = len([m for m in metadatas if m["has_elec_heating"]])
        anomalies_count = len([m for m in metadatas if m["anomaly_date"]])
        both_count = len(
            [m for m in metadatas if m["anomaly_date"] and m["has_elec_heating"]]
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Number of clients: {len(metadatas)}
        Electricity heating count: {elec_heating_count}
        Anomalies count: {anomalies_count}
        Electricity heating and anomalies count: {both_count}
        """
            )
        )
