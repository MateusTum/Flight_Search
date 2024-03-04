from django.contrib import admin
from .models import MonitoredFlight

@admin.register(MonitoredFlight)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'alert_email', 'date_from', 'date_to', 'best_flight')
