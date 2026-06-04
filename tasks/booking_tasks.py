# tasks/booking_tasks.py

from crewai import Task
from agents.travel_agents import (
    flight_agent,
    seat_agent,
    meal_agent,
    ticket_agent
)

flight_task = Task(
    description="""
    User wants to travel:

    Source: New York
    Destination: London
    Date: 2026-08-15
    Class: Business

    Available Flights:

    AI101 - $1200
    BA205 - $1100
    UA300 - $1300

    Select the best flight and explain why.
    """,
    expected_output="""
    Selected flight with reasoning.
    """,
    agent=flight_agent
)

seat_task = Task(
    description="""
    The traveler prefers a window seat.

    Recommend the best available seat.
    """,
    expected_output="""
    Seat selection with reasoning.
    """,
    agent=seat_agent
)

meal_task = Task(
    description="""
    The traveler prefers vegetarian food.

    Recommend the best meal option.
    """,
    expected_output="""
    Meal recommendation.
    """,
    agent=meal_agent
)

ticket_task = Task(
    description="""
    Create a final travel summary using:

    - Selected flight
    - Seat selection
    - Meal recommendation

    Present it professionally.
    """,
    expected_output="""
    Complete booking summary.
    """,
    agent=ticket_agent
)