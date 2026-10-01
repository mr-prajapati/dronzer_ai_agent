from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

prompt = input("Enter your Prompt : ")

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents = prompt
)

print("The Response is ")
print("----------------")
print("----------------")

print(response.text)

print("----------------")
print("----------------")

