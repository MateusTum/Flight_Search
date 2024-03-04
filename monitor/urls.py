from django.urls import path
from .views import FlightDataView, create_monitored_flight

urlpatterns = [
    path('flight-data/', FlightDataView.as_view(), name='flight-data'),
    path('add_flight/', create_monitored_flight, name='add_flight'),
]