import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_gpt3(messages):
    chatbot_instructions = (
        "You are Arona(アロナ) from Blue Archive. You are talking to sensei"
    )

    messages = [
        {"role": "assistant", "content": chatbot_instructions},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("Ruilin: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        response = chat_with_gpt3(user_input)
        print("Arona: ", response)
    
