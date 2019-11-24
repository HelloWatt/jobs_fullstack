from random import random, uniform
from faker import Faker

from dashboard.models import Client, Consumption
from .constants import start_year, years, months

yearly_consumption_range = [1000, 3000]  # without heating, without anomalies
consumption_variation = 0.3  # Let's randomize a bit the consumption. Without anomalies

heating_probability = 0.3
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
    0.05  # Probability of an anomalie occuring during a year
)
anomaly_probability_each_month = 1 - (1 - anomaly_probability_each_year) ** (
    1 / 12
)  # <=> py = 1 - (1 - pm) ** 12
anomaly_increase_range = [0.9, 1.5]


def generate_consumptions(nb_clients):
    fake = Faker()
    consumptions = []
    metadatas = []
    clients = []
    consumption_pk = 1

    for client_pk in range(1, nb_clients + 1):
        client = Client(pk=client_pk, full_name=fake.name())

        yearly_consumption = uniform(
            yearly_consumption_range[0], yearly_consumption_range[1]
        )
        actual_anomaly_impact = 0  # 0 = no anomaly
        has_elec_heating = random() < heating_probability
        client_heating_ratio = [
            max(1, uniform(ratio - heating_variation, ratio + heating_variation))
            for ratio in heating_ratio
        ]
        metadata = {"client_id": client_pk, "has_elec_heating": has_elec_heating, "anomaly_date": None}

        for year in years:
            for month in months:
                kwh_consumed = yearly_consumption / 12
                kwh_consumed = uniform(
                    kwh_consumed * (1 - consumption_variation),
                    kwh_consumed * (1 + consumption_variation),
                )
                kwh_consumed *= 1 + actual_anomaly_impact
                if has_elec_heating:
                    kwh_consumed *= client_heating_ratio[month - 1]

                consumptions.append(
                    Consumption(
                        pk=consumption_pk,
                        client=client,
                        kwh_consumed=kwh_consumed,
                        month=month,
                        year=year,
                    )
                )
                consumption_pk += 1

                if (
                    not actual_anomaly_impact
                    and random() < anomaly_probability_each_month
                ):
                    actual_anomaly_impact = uniform(
                        anomaly_increase_range[0], anomaly_increase_range[1]
                    )
                    metadata["anomaly_date"] = {"month": month, "year": year}
        
        metadatas.append(metadata)
        clients.append(client)

    return consumptions, clients, metadatas
