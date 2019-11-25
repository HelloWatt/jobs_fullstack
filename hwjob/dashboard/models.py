from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
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
        return (
            f"Conso of {self.client} ({self.month}/{self.year}): {self.kwh_consumed}"
        )

    def get_absolute_url(self):
        return reverse("dashboard:consumption_details", kwargs={"client_id": self.pk})


class ElectricityPrice(MonthMixin):
    """
        Store the electricity price during a month
    """

    cteuro_per_kwh = models.FloatField("price ct€/kwh")

    class Meta:
        verbose_name = "Electricity price"
        verbose_name_plural = "Electricity prices"
        unique_together = ("month", "year")

    def __str__(self):
        return f"Elec price ({self.month}/{self.year}): {self.cteuro_per_kwh}"
