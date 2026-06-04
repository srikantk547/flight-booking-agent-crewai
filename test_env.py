from dotenv import load_dotenv
import os

load_dotenv()

print("API Key Exists:", bool(os.getenv("OPENROUTER_API_KEY")))
print("Model:", os.getenv("MODEL"))