# agents/llm_config.py

from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model=f"openrouter/{os.getenv('MODEL')}",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)