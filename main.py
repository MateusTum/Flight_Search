from modules import data_manager
from modules import flight_data
from modules import flight_search
# from modules import notification_manager
import os

FLIGHT_API_KEY = os.getenv('FLIGHT_API_KEY')
csv_flights_filepath = os.getenv('csv_flights_filepath')
city_from = "BSB"
date_from = "04/10/2023"
date_to = "04/04/2024"

DataManager = data_manager.DataManager(csv_flights_filepath=csv_flights_filepath)
FlightSearch = flight_search.FlightSearch(api_key=FLIGHT_API_KEY)
FlightData = flight_data.FlightData()

IATA_destinies = DataManager.csv_as_dict()

for city_key in IATA_destinies:
    latest_flight_info = FlightSearch.get_flight_data(fly_from=city_from, date_from=date_from,
                                                      date_to=date_to, iata_code=IATA_destinies[city_key]["IATA Code"],
                                                      city=IATA_destinies[city_key]["City Name"])

    best_price = FlightData.structure_data(flight_data=latest_flight_info)[-2]
    last_price = IATA_destinies[city_key]["Lowest Price"]

    if data_manager.check_for_lower_price(best_price=best_price, last_price=last_price):
        DataManager.update_df(city=IATA_destinies[city_key]["City Name"], new_price=best_price)
        DataManager.save_google_sheet()
        # Todo: Send notification
        # NotificationManager.send_notification(city=city_key["City Name"], new_price=best_price)