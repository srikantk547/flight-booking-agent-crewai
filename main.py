# main.py

from crewai import Crew, Process

from agents.travel_agents import (
    flight_agent,
    seat_agent,
    meal_agent,
    ticket_agent
)

from tasks.booking_tasks import (
    flight_task,
    seat_task,
    meal_task,
    ticket_task
)

crew = Crew(
    agents=[
        flight_agent,
        seat_agent,
        meal_agent,
        ticket_agent
    ],
    tasks=[
        flight_task,
        seat_task,
        meal_task,
        ticket_task
    ],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\n")
print("=" * 50)
print("FINAL BOOKING RESULT")
print("=" * 50)
print(result)