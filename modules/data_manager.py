import pandas as pd


def check_for_lower_price(best_price, last_price):
    if best_price < last_price:
        print("Found a lower price")
        return True
    else:
        print("Found a higher price")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, csv_flights_filepath):
        self.csv_flights_filepath = csv_flights_filepath
        self.sheets_df = self.get_dataframe()
        self.updated_sheets_df = self.sheets_df.copy()

    def get_dataframe(self):
        with open(self.csv_flights_filepath, 'r') as data:
            df = pd.read_csv(data)
        return df

    def csv_as_dict(self):
        cities_of_destiny = {}
        for index, row in self.sheets_df.iterrows():
            city = row["City"]
            iata_code = row["IATA Code"]
            latest_price = row["Lowest Price"]
            cities_of_destiny[city] = {"City Name": city, "IATA Code": iata_code, "Lowest Price": latest_price}
        return cities_of_destiny

    def update_df(self, city, new_price):
        print("Updating dataframe with a lower price...")
        self.updated_sheets_df.loc[self.updated_sheets_df['City'] == city, 'Lowest Price'] = new_price

    def save_google_sheet(self):
        print("Saving dataframe as csv file")
        self.updated_sheets_df.to_csv(self.csv_flights_filepath, index=False)
