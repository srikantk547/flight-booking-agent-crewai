# agents/travel_agents.py

from crewai import Agent
from agents.llm_config import llm

flight_agent = Agent(
    role="Flight Search Specialist",
    goal="Find the best available flight",
    backstory="""
    You are an airline booking specialist.
    Compare flights and select the best option
    based on user requirements.
    """,
    llm=llm,
    verbose=True
)

seat_agent = Agent(
    role="Seat Selection Specialist",
    goal="Select the best seat",
    backstory="""
    You specialize in passenger comfort and
    seat optimization.
    """,
    llm=llm,
    verbose=True
)

meal_agent = Agent(
    role="Meal Selection Specialist",
    goal="Recommend the best meal",
    backstory="""
    You are an airline catering expert.
    """,
    llm=llm,
    verbose=True
)

ticket_agent = Agent(
    role="Ticket Generation Specialist",
    goal="Generate final booking summary",
    backstory="""
    You create professional travel itineraries.
    """,
    llm=llm,
    verbose=True
)