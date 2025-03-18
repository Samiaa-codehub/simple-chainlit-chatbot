import os 
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)

@cl.on_chat_start
async def on_chart_start():
    await cl.Message(content="Hello! I am a chatbot. Ask me anything!").send()

@cl.on_message
async def on_message(message: cl.Message):
    
    prompt = message.content

    response = model.generate_content(prompt)


    response_text = response.text if hasattr(response, "text") else ""


    await cl.Message(content=response_text).send()