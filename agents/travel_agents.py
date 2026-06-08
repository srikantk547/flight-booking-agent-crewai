# agents/travel_agents.py

from crewai import Agent
from agents.llm_config import llm

coordinator_agent = Agent(
    role="Travel Coordinator",
    goal="Manage the entire booking workflow",
    backstory="""
    You are responsible for coordinating all
    travel booking activities and ensuring
    the booking is completed successfully.
    """,
    llm=llm,
    verbose=True
)

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
    You MUST return valid JSON only.

    Example:

    {
      "seat_number": "21A"
    }

    Do not add explanations.
    Do not add markdown.
    """,
    llm=llm,
    verbose=True
)

meal_agent = Agent(
    role="Meal Selection Specialist",
    goal="Recommend meal",
    backstory="""
You must return ONLY:

{
  "meal_name": "Vegetarian Meal"
}

No descriptions.
No nutritional information.
No markdown.
No extra fields.
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

payment_agent = Agent(
    role="Payment Processing Specialist",
    goal="Process flight payment",
    backstory="""
    You process payments for flight bookings.

    Return ONLY valid JSON.

    Example:

    {
        "payment_status": "SUCCESS",
        "transaction_id": "TXN001"
    }
    """,
    llm=llm,
    verbose=True
)