from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class FlightDataView(APIView):
    def get(self, request, *args, **kwargs):
        # get user inputs
        destination = request.query_params.get('destination')
        departure_date = request.query_params.get('departure_date')
        api_key = request.query_params.get('api_key')
        params = request.query_params.get('params')

        api_url = "https://api.tequila.kiwi.com/v2/search"
        headers = {'apikey': f'{api_key}'}
        params = {
        'fly_from': params.fly_from,
        'fly_to': params.fly_to,
        'date_from': params.date_from,
        'date_to': params.date_to
        }

        # Make the request to the third-party API
        response = requests.get(api_url, headers=headers, params=params)

        # Handle the response
        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({'error': 'Failed to fetch data from the third-party API'}, status=response.status_code)

