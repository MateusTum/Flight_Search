class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data = None

    def structure_data(self, flight_data):
        self.flight_data = flight_data

        def convert_duration_to_hours(duration):
            duration_in_minutes = duration / 60
            duration_in_hours = duration_in_minutes / 60
            return duration_in_hours

        city_of_departure = self.flight_data["data"][0]["cityFrom"]
        departure_iata = self.flight_data["data"][0]["flyFrom"]
        city_of_destiny = self.flight_data["data"][0]["cityTo"]
        destiny_iata = self.flight_data["data"][0]["flyTo"]
        local_date_of_departure = self.flight_data["data"][0]["local_departure"]
        utc_date_of_departure = self.flight_data["data"][0]["utc_departure"]
        local_date_of_arrival = self.flight_data["data"][0]["local_arrival"]
        utc_date_of_arrival = self.flight_data["data"][0]["utc_arrival"]
        airline = self.flight_data["data"][0]["airlines"]
        duration_of_flight = convert_duration_to_hours(self.flight_data["data"][0]["duration"]["departure"])
        best_price = self.flight_data["data"][0]["price"]
        currency = self.flight_data["currency"]

        return (city_of_departure, departure_iata, city_of_destiny, destiny_iata, local_date_of_departure,
                utc_date_of_departure, local_date_of_arrival, utc_date_of_arrival, airline, duration_of_flight,
                best_price,
                currency)
