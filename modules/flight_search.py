import requests
# import json


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key):
        self.api_key = api_key
        self.FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

    def get_flight_data(self, fly_from, date_from, date_to, iata_code, city):
        headers = {
            "apikey": self.api_key
        }

        params = {
            "fly_from": fly_from,
            "fly_to": iata_code,
            "date_from": date_from,
            "date_to": date_to
        }

        response = requests.get(url=self.FLIGHT_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        json_data = response.json()

        # Uncomment these lines below (and import json) if access to json files containing flights information is needed
        # output_name = city
        # with open(f"data_output/{output_name}_output.json", "w") as flight_output:
        #     json.dump(json_data, flight_output, indent=4)
        return json_data
