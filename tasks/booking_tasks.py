from crewai import Task

from agents.travel_agents import (
    flight_agent,
    seat_agent,
    meal_agent,
    ticket_agent
)


def create_tasks(booking):

    flight_task = Task(
        description=f"""
    Select best flight.

    Source: {booking.source}
    Destination: {booking.destination}

    Flights:

    AI101 - $1200
    BA205 - $1100
    UA300 - $1300

    Return ONLY valid JSON.

    {{
        "flight_number": "",
        "price": 0
    }}
    """,
        expected_output="Valid JSON",
        agent=flight_agent
    )

    seat_task = Task(
        description=f"""
    Flight:

    {booking.selected_flight}

    Seat Preference:

    {booking.seat_preference}

    Return ONLY valid JSON.

    {{
        "seat_number": ""
    }}
    """,
        expected_output="Valid JSON",
        agent=seat_agent
    )

    meal_task = Task(
        description=f"""
    Flight:

    {booking.selected_flight}

    Meal Preference:

    {booking.meal_preference}

    Return ONLY valid JSON.

    {{
        "meal_name": ""
    }}

    Do not return any additional fields.
    """,
        expected_output="Valid JSON",
        agent=meal_agent
    )

    ticket_task = Task(
        description="""
        Create a professional travel itinerary
        using previous task outputs.
        """,
        expected_output="Final booking summary.",
        agent=ticket_agent
    )

    return [
        flight_task,
        seat_task,
        meal_task,
        ticket_task
    ]