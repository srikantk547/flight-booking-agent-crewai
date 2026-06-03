from crewai import Crew
from agents import (
    flight_search_agent,
    seat_agent,
    meal_agent,
    ticket_agent
)

from tasks import (
    search_task,
    seat_task,
    meal_task,
    ticket_task
)

from flights import flights


def search_flight(source, destination, date, travel_class):

    for flight in flights:

        if (
            flight["source"] == source
            and flight["destination"] == destination
            and flight["date"] == date
            and flight["class"] == travel_class
        ):
            return flight

    return None


source = input("Source City: ")
destination = input("Destination City: ")
date = input("Journey Date (YYYY-MM-DD): ")
travel_class = input("Class (Economy/Business): ")
seat_pref = input("Seat Preference: ")
meal_pref = input("Meal Preference: ")
email = input("Email: ")


flight = search_flight(
    source,
    destination,
    date,
    travel_class
)

if not flight:
    print("No flights found")
    exit()


crew = Crew(
    agents=[
        flight_search_agent,
        seat_agent,
        meal_agent,
        ticket_agent
    ],
    tasks=[
        search_task,
        seat_task,
        meal_task,
        ticket_task
    ],
    verbose=True
)

result = crew.kickoff()

print("\n")
print("======== TICKET ========")

print(f"Flight Number: {flight['flight_no']}")
print(f"Source: {source}")
print(f"Destination: {destination}")
print(f"Date: {date}")
print(f"Class: {travel_class}")
print(f"Seat: {seat_pref}")
print(f"Meal: {meal_pref}")
print(f"Email: {email}")
print(f"Price: ${flight['price']}")

print("========================")