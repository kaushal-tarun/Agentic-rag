import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from backend.models.route import RouteDecision

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def decide_route(message: str) -> RouteDecision:
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=f"""
You are a router.

Choose exactly one route:

- calculator
- chat

User message:
{message}
""",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=RouteDecision,
        ),
    )

    return response.parsed