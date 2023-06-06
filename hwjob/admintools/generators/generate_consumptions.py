from random import random, shuffle, uniform

from dateutil.relativedelta import relativedelta
from faker import Faker

from dashboard.models import Client, Consumption

from .constants import end_date, start_date

yearly_consumption_range = [1000, 3000]  # without heating, without anomalies
consumption_variation = 0.3

heating_probability = 0.4
heating_ratio = [
    4.6,  # jan
    3.9,  # fab
    3.1,  # mar
    2.2,  # apr
    1.2,  # may
    1,  # june
    1,  # jul
    1,  # aug
    1.3,  # sept
    1.9,  # oct
    2.5,  # nov
    3.3,  # dec
]
heating_variation = 0.3  # Each client has a different heating profile

anomaly_probability_each_year = (
    0.04  # Probability of an anomalie occuring during a year
)
anomaly_probability_each_month = 1 - (1 - anomaly_probability_each_year) ** (
    1 / 12
)  # <=> py = 1 - (1 - pm) ** 12
anomaly_increase_range = [0.9, 1.5]

zero_conso_probability = 0.01
hole_in_conso_probability = 0.05
hole_probability = 0.2


def generate_consumptions(nb_clients):
    # The first three clients are crafted, the rest is random
    # client 1: no heating, no anomaly
    # client 2: heating, no anomaly
    # client 3: heating, anomaly
    fake = Faker()
    consumptions = []
    metadatas = []
    clients = []
    for i in range(1, nb_clients + 1):
        client = Client.objects.create(full_name=fake.name())

        yearly_consumption = uniform(
            yearly_consumption_range[0], yearly_consumption_range[1]
        )
        anomaly_offset = 0  # 0 = no anomaly
        if i == 0:
            has_elec_heating = False
        elif i in [1, 2]:
            has_elec_heating = True
        else:
            has_elec_heating = random() < heating_probability
        client_heating_ratio = [
            max(1, uniform(ratio - heating_variation, ratio + heating_variation))
            for ratio in heating_ratio
        ]
        metadata = {
            "client_id": client.id,
            "has_elec_heating": has_elec_heating,
            "anomaly_date": None,
        }
        has_conso = i > 2 and not (random() < zero_conso_probability)
        has_hole_in_conso = i > 2 and random() < hole_in_conso_probability
        iter_date = start_date
        while has_conso and iter_date <= end_date:
            if has_hole_in_conso and random() < hole_probability:
                continue
            kwh_consumed = yearly_consumption / 12
            kwh_consumed = uniform(
                kwh_consumed * (1 - consumption_variation),
                kwh_consumed * (1 + consumption_variation),
            )
            kwh_consumed *= 1 + anomaly_offset
            if has_elec_heating:
                kwh_consumed *= client_heating_ratio[iter_date.month - 1]

            consumptions.append(
                Consumption(
                    client=client,
                    kwh_consumed=kwh_consumed,
                    month=iter_date.month,
                    year=iter_date.year,
                )
            )

            if (
                not anomaly_offset
                and i != 0
                and (random() < anomaly_probability_each_month or i in [1, 2])
            ):
                anomaly_offset = uniform(
                    anomaly_increase_range[0], anomaly_increase_range[1]
                )
                metadata["anomaly_date"] = {
                    "month": iter_date.month,
                    "year": iter_date.year,
                }

            iter_date += relativedelta(months=1)
        metadatas.append(metadata)
        clients.append(client)

    shuffle(consumptions)
    Consumption.objects.bulk_create(consumptions)
    return metadatas
