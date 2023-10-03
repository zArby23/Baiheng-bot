from interactions import Client, Intents, Status, listen
from interactions.api.events import MessageCreate
import token_1

bot = Client(intents=Intents.DEFAULT,
             status=Status.IDLE,
             activity="WIP")

@listen()
async def on_ready():
    print("Baiheng's ready!")

@listen(MessageCreate)
async def on_message_create(event: MessageCreate):
    print(f"Message received: {event.message.content}")

bot.start(f"{token_1.token_}")

