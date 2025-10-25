import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import chainlit as cl

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
@cl.on_chat_start
async def handle_start():
    await cl.Message(content="My Chatbot!").send()


@cl.on_message
async def handle_message(message: cl.Message):
    try:
        result = await external_client.chat.completions.create(
            model= "gemini-2.0-flash",
            messages = [{"role":"user", "content": message.content}],
        )
        await cl.Message(content=result.choices[0].message.content).send()
    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()

    
    



