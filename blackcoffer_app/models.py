from django.db import models


class Sale(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.product}"


class Event(models.Model):
    intensity = models.IntegerField()
    likelihood = models.IntegerField()
    relevance = models.IntegerField()
    year = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"Event {self.id}"

# visualization_app/models.py
from django.db import models

class DataPoint(models.Model):
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    pest = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    swot = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year} - {self.country}"
