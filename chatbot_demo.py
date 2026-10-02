from google import genai
from google.genai  import  types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

print("Chat Starts here.......Type 'endchat' to close the chat")

userinput = input("User : ")

while userinput != 'endchat' :
    systemoutput = client.models.generate_content(
        contents = userinput ,
        model = 'gemini-3.5-flash' ,
        config = types.GenerateContentConfig(
            system_instruction = "Answer in 1 line within 50 characters"
        )
    )
    for part in systemoutput.parts:
        if part.text and not getattr(part, "thought", False):
         print("Dronzer : ",part.text)
         userinput = input("User : ")
