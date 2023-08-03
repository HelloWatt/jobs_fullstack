import statistics

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import OuterRef, Sum, Case, When, F, Subquery
from django.urls import reverse



class MonthMixin(models.Model):
    month = models.PositiveSmallIntegerField(
        "month", validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    year = models.PositiveSmallIntegerField("year")

    class Meta:
        abstract = True


class Client(models.Model):
    full_name = models.CharField("full name", max_length=50)

    def has_elec_heating(self):
        cold_months = list(self.consumption_set.filter(month__in=[11, 12, 1, 2, 3, 4]).values_list("kwh_consumed", flat=True))
        hot_months = list(self.consumption_set.filter(month__in=[5, 6, 7, 8, 9, 10]).values_list("kwh_consumed", flat=True))
        cold_months_average_consumption =  statistics.mean(cold_months)
        hot_months_average_consumption =  statistics.mean(hot_months)

        return cold_months_average_consumption > 2 * hot_months_average_consumption


    def __str__(self):
        return f"Client {self.pk}"


class Consumption(MonthMixin):
    """
    Store the electricity consumption of a client over a month
    """

    client = models.ForeignKey(
        "dashboard.Client", verbose_name="client", on_delete=models.CASCADE
    )
    kwh_consumed = models.FloatField("kwh consumed")

    class Meta:
        verbose_name = "Consumption"
        verbose_name_plural = "Consumptions"
        unique_together = ("client", "month", "year")

    def __str__(self):
        return f"Conso of {self.client} ({self.month}/{self.year}): {self.kwh_consumed}"

    def get_absolute_url(self):
        return reverse("dashboard:consumption_details", kwargs={"client_id": self.pk})

