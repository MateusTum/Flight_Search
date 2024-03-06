from django.db import models
from flights.models import Flight

# Create your models here.

class MonitoredFlight(models.Model):
    name = models.CharField(max_length=30)
    alert_email = models.EmailField(max_length=50)

    IATA_departure = models.CharField(max_length=3)
    IATA_arrival = models.CharField(max_length=3)

    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    best_flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='best_flight', null=True, blank=True)

    def __str__(self):
        return self.name