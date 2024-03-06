from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.shortcuts import render, redirect
from .forms import MonitoredFlightForm
from django.urls import reverse
from monitor.models import MonitoredFlight
from flights.models import Flight
from .forms import ApiKeyForm
import json
import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import make_aware
import pytz

def create_monitored_flight(request):
    if request.method == 'POST':
        form = MonitoredFlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MonitoredFlightForm()
    return render(request, 'monitor/add_flight.html', {'form': form})

def index(request):
    flights = MonitoredFlight.objects.all()
    if request.method == 'POST':
        form = ApiKeyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')  # Redirect to a new URL if the form is successfully processed
    else:
        form = ApiKeyForm()
    return render(request, 'monitor/index.html', {'flights': flights, 'form': form})


def check_flights(request):
    def generate_flight():
        name = f"name"
        price = 0  # Assuming the price is between 50 and 1000 for the example

        # Generate random dates for departure and arrival
        now = timezone.now()
        departure_date = now + timedelta(days=random.randint(1, 30))
        arrival_date = departure_date + timedelta(hours=random.randint(1, 12))

        flight_duration = random.randint(1, 12)
        flight_distance = random.randint(300, 4000)

        destination_airport = f"Airport {random.choice(['A', 'B', 'C', 'D'])}"
        departure_airport = f"Airport {random.choice(['E', 'F', 'G', 'H'])}"

        new_flight = Flight.objects.create(
            name=name,
            price=price,
            departure_date=departure_date,
            arrival_date=arrival_date,
            flight_duration=flight_duration,
            flight_distance=flight_distance,
            destination_airport=destination_airport,
            departure_airport=departure_airport
        )

        return new_flight

    def find_best_flight_deal(flight_data):
        # Initialize variables to store the best flight details
        best_price = float('inf')
        best_flight = None

        # Iterate through each flight option in the JSON data
        for flight in flight_data['data']:
            # Check if the current flight has a lower price than the current best
            if flight['price'] < best_price:
                best_price = flight['price']
                best_flight = flight
            elif flight['price'] == best_price:
                # If the price is the same, prefer shorter duration or higher quality
                if 'duration' in flight and flight['duration']['total'] < best_flight['duration']['total']:
                    best_flight = flight
                elif 'quality' in flight and flight['quality'] > best_flight['quality']:
                    best_flight = flight

        return best_flight
    
    def process_response(response, flight):
        if response.status_code == 200:
            data = response.json()
            return True, data
        else:
            message = f"Failed to get flight data for {flight.name}. Status code: {response.status_code}"
            return False, message

    def create_flight_deal():
        flight_object = generate_flight()
        best_flight_deal = find_best_flight_deal(result)
        flight_object.name = f"{best_flight_deal['flyFrom']} to {best_flight_deal['flyTo']}"
        flight_object.price = int(best_flight_deal['price'])
        flight_object.departure_airport = best_flight_deal['flyFrom']
        flight_object.destination_airport = best_flight_deal['flyTo']
        flight_object.offer_link = best_flight_deal['deep_link']
        flight_object.departure_date = convert_time(best_flight_deal['local_departure'])
        flight_object.arrival_date = convert_time(best_flight_deal['local_arrival'])
        flight_object.save()
        flight.best_flight = flight_object
        flight.save()

    def convert_time(string):
        date_str = string
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        date_obj_aware = make_aware(date_obj, pytz.UTC)

        return date_obj_aware

    # Get all monitored flights
    monitored_flights = MonitoredFlight.objects.all()

    # Get api_key from body
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    api_key = body.get('api_key', '')

    # Server url
    base_url = 'http://localhost:8000/monitor/flight-data/'

    # Third party api url
    api_url = "https://api.tequila.kiwi.com/v2/search/"

    # Headers
    headers = {'apikey': api_key}

    for flight in monitored_flights:
        params = {
                'api_key': api_key,
                'fly_from': flight.IATA_departure,
                'fly_to': flight.IATA_arrival,
                'date_from': flight.date_from.strftime('%d/%m/%Y'),
                'date_to': flight.date_to.strftime('%d/%m/%Y'),
            }
             
        # Send request to 3rd party API
        response = requests.get(api_url, headers=headers, params=params)

        # Process response
        success, result = process_response(response, flight)

        if success:
            print("Flight data retrieved successfully. Creating flight for flight deal")
            create_flight_deal()
        else:
            return("Error:", result)
    return JsonResponse({'success': True, 'message': 'Flights checked and updated.'})