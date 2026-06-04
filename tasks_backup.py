from crewai import Task
from agents import (
    flight_search_agent,
    seat_agent,
    meal_agent,
    ticket_agent
)

search_task = Task(
    description="""
    Search a flight matching user criteria.
    Return flight details.
    """,
    agent=flight_search_agent,
    expected_output="Flight details"
)

seat_task = Task(
    description="""
    Assign seat based on preference.
    """,
    agent=seat_agent,
    expected_output="Seat assigned"
)

meal_task = Task(
    description="""
    Assign meal based on preference.
    """,
    agent=meal_agent,
    expected_output="Meal assigned"
)

ticket_task = Task(
    description="""
    Generate final travel ticket.
    """,
    agent=ticket_agent,
    expected_output="Complete ticket"
)