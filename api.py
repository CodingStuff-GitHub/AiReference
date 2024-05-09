import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv("./config.env")

genai.configure(api_key=os.environ["GEMINI_KEY"])
model = genai.GenerativeModel("gemini-pro")

# Generate content
# response = model.generate_content("Write a poem about unicorns")
# print(response.text)

# Start Chatting
model.start_chat()
chat = model.start_chat()
inp = ""
while inp != "STOP":
    inp = input(">>> ")
    if inp:
        response = chat.send_message(inp)
        print(response.text)
