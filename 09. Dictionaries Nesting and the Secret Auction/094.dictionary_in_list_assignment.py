travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Munich", "Frankfurt", "Hamburg"],
    },
]


def add_new_country(country_name, visit_times, city_name):
    new_country = {"country": country_name,
                   "visits": visit_times,
                   "cities": city_name,
                   }
    travel_log.append(new_country)

    # another way to do that:
    # new_country = {}
    # new_country["country"] = country_name
    # new_country["visits"] = visit_times
    # new_country["cities"] = city_name


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
