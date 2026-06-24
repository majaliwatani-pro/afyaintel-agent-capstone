import os
from dotenv import load_dotenv
from google import genai

load_dotenv("../../.env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to the .env file in the main course folder.")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain AI agents in 3 simple bullet points."
)

print(response.text)