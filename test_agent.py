from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model=f"openrouter/{os.getenv('MODEL')}",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    role="Travel Assistant",
    goal="Help users plan trips",
    backstory="You are an expert travel advisor.",
    llm=llm,
    verbose=True
)

task = Task(
    description="""
    Say hello and explain what a flight booking agent does.
    """,
    expected_output="A short explanation.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

print("\nRESULT:")
print(result)