from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class FlightDataView(APIView):
    def get(self, request, *args, **kwargs):
        # Functions
        def remove_api_key_from_params(params):
            params.pop('api_key')
            filtered_params = all_params
            print(filtered_params)
            return filtered_params

        # User inputs
        all_params = request.query_params.dict()

        api_url = "https://api.tequila.kiwi.com/v2/search"
        headers = {'apikey': f'{all_params['api_key']}'}

        # Make the request to the third-party API
        response = requests.get(api_url, headers=headers, params=all_params.pop('api_key'))

        # Handle the response
        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({'error': 'Failed to fetch data from the third-party API'}, status=response.status_code)