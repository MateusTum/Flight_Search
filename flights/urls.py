from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, AirportViewSet, FlightViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'airports', AirportViewSet)
router.register(r'flights', FlightViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
