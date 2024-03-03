from django.contrib import admin
from .models import City, Airport, Flight

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'code', 'timezone', 'population')

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'iata_code', 'city')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('departure_date', 'arrival_date', 'flight_duration', 'flight_distance', 'destination_airport', 'departure_airport', 'created_at', 'updated_at')
