from crewai import Agent, Task, Crew
from agents.llm_config import llm

agent = Agent(
    role="JSON Flight Agent",
    goal="Return structured flight data",
    backstory="You return JSON only.",
    llm=llm
)

task = Task(
    description="""
    Choose the best flight.

    Flights:

    AI101 - $1200
    BA205 - $1100
    UA300 - $1300

    Return ONLY valid JSON:

    {
      "flight_number": "...",
      "price": ...
    }
    """,
    expected_output="Valid JSON",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task]
)

result = crew.kickoff()

print(result)