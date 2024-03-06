from django.urls import path
from .views import create_monitored_flight, check_flights


urlpatterns = [
    path('add_flight/', create_monitored_flight, name='add_flight'),
    path('check-flights/', check_flights, name='check_flights'),
]