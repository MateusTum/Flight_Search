from django.urls import path
from .views import FlightDataView

urlpatterns = [
    path('flight-data/', FlightDataView.as_view(), name='flight-data'),
]
