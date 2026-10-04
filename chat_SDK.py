from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash")
print("Chat Starts here.......Type endchat to stop & exit")
userinput = input("User : ")
while userinput != 'endchat' :
    response = chat.send_message(userinput)
    for part in response.parts:
        if getattr(part, "text", None) and not getattr(part, "thought", False):
            print("DRONZER :", part.text)
    userinput = input("User :") 
