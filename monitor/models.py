from django.db import models
from flights.models import Flight

# Create your models here.

class MonitoredFlight(models.Model):
    name = models.CharField(max_length=30)

    date_from = models.DateField()
    date_to = models.DateField()

    best_flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='best_flight', null=True, blank=True)

    def __str__(self):
        return self.name