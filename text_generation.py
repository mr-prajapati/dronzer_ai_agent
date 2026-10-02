from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
from PIL import Image

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

# prompt = input("Enter your Prompt : ")
image = Image.open("Image/Cat.jpg")
response = client.models.generate_content(
    model='gemini-3.5-flash',
    # contents = prompt ,
    contents = [image , "Tell me about this image"],
    config = types.GenerateContentConfig(
        system_instruction = "Response should be in 20 words and be funny" 
    )
)

print("The Response is ")
print("----------------")
print("----------------")

for part in response.parts:
    if part.text and not getattr(part, "thought", False):
        print(part.text)

print("----------------")
print("----------------")