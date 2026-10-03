# from google import genai
# from google.genai  import  types
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = genai.Client()

# print("Chat Starts here.......Type 'endchat' to close the chat")

# chat = []

# userinput = input("User : ")

# while userinput != 'endchat' :
#     chat.append("user : " + userinput)
#     systemoutput = client.models.generate_content(
#         contents = userinput ,
#         model = 'gemini-3.5-flash' ,
#         config = types.GenerateContentConfig(
#             system_instruction = "Answer in 1 line within 50 characters"
#         )
#     )
#     chat.append("DRONZER : " + systemoutput.text)

#     for part in systemoutput.parts:
#         if part.text and not getattr(part, "thought", False):
#          print("Dronzer : ",part.text)
#          userinput = input("User : ")

from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="Answer in 1 line within 50 characters"
    )
)

print("Chat Starts here.........Type 'endchat' to close the chat")

while True:
    userinput = input("User : ")

    if userinput == "endchat":
        break

    response = chat.send_message(userinput)

    for part in response.parts:
        if part.text and not getattr(part, "thought", False):
            print("Dronzer :", part.text)