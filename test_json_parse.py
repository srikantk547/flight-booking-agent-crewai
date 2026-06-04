from crewai import Agent, Task, Crew

from agents.llm_config import llm
from json_utils import parse_json_response

agent = Agent(
    role="Flight Agent",
    goal="Choose best flight",
    backstory="Return JSON only",
    llm=llm
)

task = Task(
    description="""
Choose the cheapest flight.

AI101 - $1200
BA205 - $1100
UA300 - $1300

Return ONLY:

{
  "flight_number": "...",
  "price": ...
}
""",
    expected_output="JSON",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task]
)

result = crew.kickoff()

print("\nRAW OUTPUT:")
print(result)

parsed = parse_json_response(result)

print("\nPARSED:")
print(parsed)

print("\nFLIGHT:")
print(parsed["flight_number"])