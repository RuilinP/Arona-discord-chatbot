import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(user_input: str) -> str:
    messages = [
        {"role": "assistant", "content": "You are Arona(アロナ) from Blue Archive. You are talking to sensei"},
        {"role": "user", "content": user_input}
    ]
    response = chat_with_gpt3(messages)
    return response

def chat_with_gpt3(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content.strip()
