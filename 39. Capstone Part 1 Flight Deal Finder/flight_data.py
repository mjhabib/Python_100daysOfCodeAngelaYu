from flight_search import FlightSearch


class FlightData:
    """This Class helps me to store all the cities along with the flight cost of that city in a dictionary to analyze"""

    def __init__(self):
        self.data = FlightSearch().return_data()
        self.counter = 0
        self.seprate_userful_data()

    def seprate_userful_data(self):
        city = []
        price = []
        for _ in self.data:
            city.append(self.data[self.counter]["data"][0]["cityTo"])
            price.append(self.data[self.counter]["data"][0]["price"])
            self.counter += 1

        self.city_price = {city[i]: price[i] for i in range(len(city))}

    def return_city_price(self):
        return self.city_price
