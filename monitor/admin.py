from django.contrib import admin
from .models import MonitoredFlight

@admin.register(MonitoredFlight)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_from', 'date_to', 'best_flight')
