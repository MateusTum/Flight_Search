from django import forms
from .models import MonitoredFlight

class MonitoredFlightForm(forms.ModelForm):
    alert_email = forms.EmailField(max_length=50)
    IATA_departure= forms.CharField(max_length=3)
    IATA_arrival = forms.CharField(max_length=3)
    date_from = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        help_text="Format: YYYY-MM-DD HH:MM"
    )
    date_to = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        help_text="Format: YYYY-MM-DD HH:MM"
    )

    class Meta:
        model = MonitoredFlight
        fields = ['name', 'alert_email', 'IATA_departure', 'IATA_arrival', 'date_from', 'date_to', 'best_flight']

class ApiKeyForm(forms.Form):
    api_key = forms.CharField(label="Api Key", max_length=50)
