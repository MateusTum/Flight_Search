from django.contrib import admin
from django.urls import path, include
from monitor.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('monitor/', include('monitor.urls')),
    path('flights/', include('flights.urls')),
]
