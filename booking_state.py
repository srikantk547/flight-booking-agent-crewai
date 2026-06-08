import random

class BookingState:

    def __init__(
            self,
            source,
            destination,
            journey_date,
            travel_class,
            seat_preference,
            meal_preference
    ):
        self.source = source
        self.destination = destination
        self.journey_date = journey_date
        self.travel_class = travel_class
        self.seat_preference = seat_preference
        self.meal_preference = meal_preference

        self.selected_flight = None
        self.selected_seat = None
        self.selected_meal = None
        self.flight_price = None
        self.payment_status = None
        self.transaction_id = None
        self.pnr = f"PNR{random.randint(100000,999999)}"
        self.email = None

    def display(self):
        return f"""
Source: {self.source}
Destination: {self.destination}
Date: {self.journey_date}
Class: {self.travel_class}

Flight: {self.selected_flight}
Seat: {self.selected_seat}
Meal: {self.selected_meal}
"""