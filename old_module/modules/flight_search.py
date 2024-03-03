import requests
import json


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key):
        self.api_key = api_key
        self.FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.FLIGHT_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
        self.headers = {"apikey": self.api_key}

    def get_flight_data(self, fly_from, date_from, date_to, iata_code, city):
        params = {
            "fly_from": fly_from,
            "fly_to": iata_code,
            "date_from": date_from,
            "date_to": date_to
        }
        # Todo: 1# Add new filters to search for flights
        # max_fly_duration
        # adults
        # children
        # selected cabins

        response = requests.get(url=self.FLIGHT_SEARCH_ENDPOINT, params=params, headers=self.headers)
        response.raise_for_status()
        json_data = response.json()

        # Uncomment these lines below (and import json) if access to json files containing flights information is needed
        # output_name = city
        # with open(f"data_output/{output_name}_output.json", "w") as flight_output:
        #     json.dump(json_data, flight_output, indent=4)
        return json_data

    def get_iata_codes(self, destination_city_name):
        params = {"term": destination_city_name,
                  "location_types": "city"}
        response = requests.get(url=self.FLIGHT_LOCATION_ENDPOINT, params=params, headers=self.headers)
        response.raise_for_status()
        json_data = response.json()

        return json_data
