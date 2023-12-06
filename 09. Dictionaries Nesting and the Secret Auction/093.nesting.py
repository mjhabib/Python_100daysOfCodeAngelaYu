# simple dict
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in a dict
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Munich", "Frankfurt", "Hamburg"],
}

# nest a dict in a dict
travel_log_attractions = {
    "France": {
        "Paris": "Eiffel Tower",
        "Lille": "La Vieille Bourse",
        "Dijon": "Church of Our Lady",
    },
    "Germany": {"Berlin": "Brandenburg Gate",
                "Munich": "Marienplatz",
                "Frankfurt": "Frankfurt Cathedral",
                "Hamburg": "St. Michael's Church",
                },
}

# combine nesting lists and dicts
travel_log_visits = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 11,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Munich", "Frankfurt", "Hamburg"],
        "total_visits": 5,
    },
}

# nesting a dict in a list
travel_log_country = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 11
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Frankfurt", "Hamburg"],
        "total_visits": 5
    },
]
