from random import uniform

from dashboard.models import ElectricityPrice
from .constants import start_year, years, months

start_price = 16  # 01/01/start_year
yearly_increase = 1.04  # +4%/y
monthly_increase = yearly_increase ** (1 / 12)
monthly_ratio = [
    1,  # jan
    0.98,  # fab
    0.96,  # mar
    0.93,  # apr
    0.91,  # may
    0.87,  # june
    0.83,  # jul
    0.85,  # aug
    0.87,  # sept
    0.90,  # oct,
    0.94,  # nov
    0.97,  # dec
]


def generate_prices():
    elec_prices = []
    pk = 1

    for year in years:
        for month in months:
            months_diff = (year - start_year) * 12 + (month - 1)
            inflation = monthly_increase ** months_diff
            expected_price = start_price * inflation * monthly_ratio[month - 1]
            random_price = uniform(expected_price - 0.3, expected_price + 0.3)

            elec_prices.append(
                ElectricityPrice(
                    pk=months_diff + 1,
                    cteuro_per_kwh=random_price,
                    month=month,
                    year=year,
                )
            )
            pk += 1

    return elec_prices
