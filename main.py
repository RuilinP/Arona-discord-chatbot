from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

from responses import get_response

load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True 
client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message empty!')
        return
    try:
        response = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    bot_mentioned = client.user.mentioned_in(message) if message.mentions else False
    
    if bot_mentioned:
        username = str(message.author)
        user_message = message.content
        channel = str(message.channel)

        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)

def main() -> None:
    client.run(token=DISCORD_TOKEN)

if __name__ == '__main__':
    main()
