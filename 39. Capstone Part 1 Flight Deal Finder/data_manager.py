from flight_data import FlightData
import pandas


class DataManager:
    """This Class will compare the cost of a flight with given costs of the same flight in our "flight_deals_csv" to see if it can find a cheap deal for us."""
    def __init__(self):
        self.data_dict = FlightData().return_city_price()
        self.compare_price()

    def compare_price(self):
        data = pandas.read_csv("flight_deals.csv", index_col=0)
        deals_dict = data.to_dict(orient="dict")

        print(f"My deals:\n {deals_dict['Lowest Price']}\n")
        print(f"Kiwi's deals (months-> 3 / limit-> 500):\n {self.data_dict}\n")

        for value in deals_dict["Lowest Price"]:
            for key in self.data_dict:
                if value == key and deals_dict["Lowest Price"][value] > self.data_dict[value]:
                    print(f"Cheap deals:\n {value}: {self.data_dict[value]}")




