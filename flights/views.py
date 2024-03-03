from rest_framework import viewsets
from .models import City, Airport, Flight
from .serializers import CitySerializer, AirportSerializer, FlightSerializer

class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    queryset = City.objects.all()
    serializer_class = CitySerializer

class AirportViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class FlightViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
