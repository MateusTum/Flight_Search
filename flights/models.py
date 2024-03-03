from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    code = models.CharField(max_length=4)
    timezone = models.CharField(max_length=50)
    population = models.IntegerField()

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=30)
    iata_code = models.CharField(max_length=3)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')

    def __str__(self):
        return self.name


class Flight(models.Model):
    # Departure / arrival
    departure_date = models.DateTimeField("Departure Date")
    arrival_date = models.DateTimeField("Arrival Date")

    # Flight information
    flight_duration = models.IntegerField("Flight Duration")
    flight_distance = models.IntegerField("Flight Distance")

    # Airports
    destination_airport = models.OneToOneField(City, on_delete=models.CASCADE, related_name='destination_airport')
    departure_airport = models.OneToOneField(City, on_delete=models.CASCADE, related_name='departure_airport')


    #Flight creation/update date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

