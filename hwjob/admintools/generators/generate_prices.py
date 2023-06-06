from random import shuffle, uniform

from dateutil.relativedelta import relativedelta

from dashboard.models import ElectricityPrice

from .constants import end_date, start_date

start_price = 16  # 01/01/start_year
yearly_increase = 1.04  # +4%/y
monthly_increase = yearly_increase ** (1 / 12)


def generate_prices():
    elec_prices = []
    iter_date = start_date
    while iter_date <= end_date:
        year = iter_date.year
        month = iter_date.month
        months_diff = (year - start_date.year) * 12 + (month - 1)
        inflation = monthly_increase**months_diff
        expected_price = start_price * inflation
        random_price = round(uniform(expected_price - 0.3, expected_price + 0.3), 2)
        elec_prices.append(
            ElectricityPrice(
                cteuro_per_kwh=random_price,
                month=month,
                year=year,
            )
        )
        print(f"{iter_date}: {random_price} ct€")
        iter_date += relativedelta(months=1)
    shuffle(elec_prices)
    ElectricityPrice.objects.bulk_create(elec_prices)
