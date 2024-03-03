from modules import data_manager
from modules import flight_data
from modules import flight_search
# from modules import notification_manager
import os

# EDIT THESE VARIABLES BELOW
FLIGHT_API_KEY = os.getenv('FLIGHT_API_KEY')
# csv_flights_filepath = os.getenv('csv_flights_filepath')
csv_flights_filepath = "cities.csv"
city_from = "BSB"
date_from = "04/10/2023"
date_to = "04/04/2024"

# DO NOT EDIT ANYTHING BELOW THIS LINE
DataManager = data_manager.DataManager(csv_flights_filepath=csv_flights_filepath)
FlightSearch = flight_search.FlightSearch(api_key=FLIGHT_API_KEY)
FlightData = flight_data.FlightData()
IATA_destinies = DataManager.destinies_csv_to_dict()

for city_key in IATA_destinies:
    city_data = FlightSearch.get_iata_codes(destination_city_name=city_key)
    city_IATA_code = data_manager.get_city_iata_code(city_data)
    DataManager.update_df_with_iata_code(city=IATA_destinies[city_key]["City Name"], city_iata_code=city_IATA_code)
    DataManager.save_google_sheet()

for city_key in IATA_destinies:
    latest_flight_info = FlightSearch.get_flight_data(fly_from=city_from, date_from=date_from,
                                                      date_to=date_to, iata_code=IATA_destinies[city_key]["IATA Code"],
                                                      city=IATA_destinies[city_key]["City Name"])

    best_price = FlightData.structure_data(flight_data=latest_flight_info)[-2]
    last_price = IATA_destinies[city_key]["Lowest Price"]

    if data_manager.check_for_lower_price(best_price=best_price, last_price=last_price):
        DataManager.update_df_with_lowest_price(city=IATA_destinies[city_key]["City Name"], new_price=best_price)
        DataManager.save_google_sheet()
        # Todo: Send notification
        # NotificationManager.send_sms_notification()
        # NotificationManager.send_email_notification()



