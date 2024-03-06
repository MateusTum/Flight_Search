from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    code = models.CharField(max_length=4, null=True)
    timezone = models.CharField(max_length=50, null=True)
    population = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=30)
    iata_code = models.CharField(max_length=3)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')

    def __str__(self):
        return self.name


class Flight(models.Model):
    name = models.CharField(max_length=60)

    price = models.IntegerField()

    # Departure / arrival
    departure_date = models.DateTimeField("Departure Date")
    arrival_date = models.DateTimeField("Arrival Date")

    # Flight information
    flight_duration = models.IntegerField("Flight Duration")
    flight_distance = models.IntegerField("Flight Distance")

    # Airports
    # destination_airport = models.OneToOneField(City, on_delete=models.CASCADE, related_name='destination_airport')
    # departure_airport = models.OneToOneField(City, on_delete=models.CASCADE, related_name='departure_airport')

    destination_airport = models.CharField(max_length=50)
    departure_airport = models.CharField(max_length=50)

    offer_link = models.TextField(default="Link here", null=True, blank=True)


    #Flight creation/update date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
