from django import forms
from .models import MonitoredFlight

class MonitoredFlightForm(forms.ModelForm):
    alert_email = forms.EmailField(max_length=50)  # Ensures only valid email addresses are accepted
    IATA_departure= forms.CharField(max_length=3)  # Max length enforced here for clarity, but should also be in the model
    IATA_arrival = forms.CharField(max_length=3)  # Max length enforced here for clarity, but should also be in the model
    date_from = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],  # Example format, adjust as needed
        help_text="Format: YYYY-MM-DD HH:MM"
    )
    date_to = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],  # Example format, adjust as needed
        help_text="Format: YYYY-MM-DD HH:MM"
    )

    class Meta:
        model = MonitoredFlight
        fields = ['name', 'alert_email', 'IATA_departure', 'IATA_arrival', 'date_from', 'date_to', 'best_flight']
