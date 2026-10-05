from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

grounding_tool = types.Tool(
      google_search = types.GoogleSearch()
)

response = client.models.generate_content(
    model = 'gemini-3.8-flash',
    contents = "Who won the ipl 2024",
    config =types.GenerateContentConfig(
          tools=[grounding_tool]
    )
)
for part in response.parts:
        if getattr(part, "text", None) and not getattr(part, "thought", False):
            print("DRONZER :", part.text)