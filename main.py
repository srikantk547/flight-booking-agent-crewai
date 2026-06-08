from crewai import Crew

from agents.travel_agents import (
    coordinator_agent,
    flight_agent,
    seat_agent,
    meal_agent,
    ticket_agent
)

from booking_state import BookingState
from booking_engine import (
    extract_flight,
    extract_seat,
    extract_meal
)

from agents.travel_agents import (
    coordinator_agent,
    flight_agent,
    seat_agent,
    meal_agent,
    payment_agent,
    ticket_agent
)

from crewai import Task

from flight_repository import get_available_flights


print("\n=== Flight Booking Agent ===\n")

source = input("Source City: ")
destination = input("Destination City: ")
journey_date = input("Journey Date (YYYY-MM-DD): ")
travel_class = input("Class (Economy/Business): ")
seat_pref = input("Seat Preference: ")
meal_pref = input("Meal Preference: ")

booking = BookingState(
    source,
    destination,
    journey_date,
    travel_class,
    seat_pref,
    meal_pref
)

print("\nSTEP 0 - Travel Coordinator\n")

from crewai import Task, Crew

coordinator_task = Task(
    description=f"""
Validate the travel request.

Source: {booking.source}
Destination: {booking.destination}
Date: {booking.journey_date}
Class: {booking.travel_class}
Seat Preference: {booking.seat_preference}
Meal Preference: {booking.meal_preference}

Confirm that booking can proceed.
""",
    expected_output="Booking validation summary",
    agent=coordinator_agent
)

coordinator_result = Crew(
    agents=[coordinator_agent],
    tasks=[coordinator_task]
).kickoff()

print(coordinator_result)

print("\nSTEP 1 - Flight Selection\n")

available_flights = get_available_flights()

flight_task = Task(
    description=f"""
Select best flight.

Source: {booking.source}
Destination: {booking.destination}

Available Flights:

{available_flights}

Return ONLY valid JSON.

{{
    "flight_number": "",
    "price": 0
}}
""",
    expected_output="JSON",
    agent=flight_agent
)

flight_result = Crew(
    agents=[flight_agent],
    tasks=[flight_task]
).kickoff()

from json_utils import parse_json_response

flight_json = parse_json_response(
    flight_result
)

booking.selected_flight = (
    flight_json["flight_number"]
)

booking.flight_price = (
    flight_json["price"]
)

print("Chosen Flight:", booking.selected_flight)

print("\nSTEP 2 - Seat Selection\n")

seat_task = Task(
    description=f"""
Flight:

{booking.selected_flight}

Seat Preference:

{booking.seat_preference}

Choose best seat.
""",
    expected_output="Selected seat",
    agent=seat_agent
)

seat_result = Crew(
    agents=[seat_agent],
    tasks=[seat_task]
).kickoff()

seat_json = parse_json_response(
    seat_result
)

booking.selected_seat = (
    seat_json["seat_number"]
)

print("Chosen Seat:", booking.selected_seat)

print("\nSTEP 3 - Meal Selection\n")

meal_task = Task(
    description=f"""
Flight:

{booking.selected_flight}

Meal Preference:

{booking.meal_preference}

Recommend meal.
""",
    expected_output="Selected meal",
    agent=meal_agent
)

meal_result = Crew(
    agents=[meal_agent],
    tasks=[meal_task]
).kickoff()

meal_json = parse_json_response(
    meal_result
)

booking.selected_meal = (
    meal_json["meal_name"]
)

print("Chosen Meal:", booking.selected_meal)


payment_task = Task(
    description=f"""
Process payment.

Flight:
{booking.selected_flight}

Amount:
${booking.flight_price}

Return ONLY valid JSON.

{{
    "payment_status": "SUCCESS",
    "transaction_id": "TXN001"
}}
""",
    expected_output="Valid JSON",
    agent=payment_agent
)

payment_result = Crew(
    agents=[payment_agent],
    tasks=[payment_task]
).kickoff()

print("\nRAW PAYMENT OUTPUT:")
print(payment_result)

payment_json = parse_json_response(
    payment_result
)

booking.payment_status = (
    payment_json["payment_status"]
)

booking.transaction_id = (
    payment_json["transaction_id"]
)

print(
    "Payment Status:",
    booking.payment_status
)

print(
    "Transaction ID:",
    booking.transaction_id
)


print("\nSTEP 5 - Ticket Generation\n")

ticket_task = Task(
    description=f"""
Generate final itinerary.

Source:
{booking.source}

Destination:
{booking.destination}

Date:
{booking.journey_date}

Flight:
{booking.selected_flight}

Seat:
{booking.selected_seat}

Meal:
{booking.selected_meal}

Payment Status:
{booking.payment_status}

Transaction ID:
{booking.transaction_id}
""",
    expected_output="Final ticket",
    agent=ticket_agent
)

ticket_result = Crew(
    agents=[ticket_agent],
    tasks=[ticket_task]
).kickoff()

print("\n")
print("=" * 60)
print("FINAL TICKET")
print("=" * 60)
print(ticket_result)