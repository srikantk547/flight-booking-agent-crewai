from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

flight_agent = Agent(
    role="Flight Search Specialist",
    goal="Choose the best flight for the traveler",
    backstory="""
    You are an experienced airline booking specialist.
    Compare flights and choose the best option.
    """,
    llm=llm,
    verbose=True
)

seat_agent = Agent(
    role="Seat Assignment Specialist",
    goal="Select the most suitable seat",
    backstory="""
    You understand passenger comfort and seat selection.
    """,
    llm=llm,
    verbose=True
)

meal_agent = Agent(
    role="Meal Coordinator",
    goal="Assign the best meal",
    backstory="""
    You specialize in airline meal planning.
    """,
    llm=llm,
    verbose=True
)

ticket_agent = Agent(
    role="Ticket Generator",
    goal="Prepare the final booking confirmation",
    backstory="""
    You create professional airline tickets.
    """,
    llm=llm,
    verbose=True
)