import json


def get_available_flights():

    with open(
            "data/flights.json",
            "r",
            encoding="utf-8"
    ) as file:

        return json.load(file)