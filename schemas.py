from pydantic import BaseModel


class FlightSelection(BaseModel):
    flight_number: str
    price: float


class SeatSelection(BaseModel):
    seat_number: str


class MealSelection(BaseModel):
    meal_name: str