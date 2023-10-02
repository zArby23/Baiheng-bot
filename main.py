from interactions import Client, Intents, Status, listen
import token_1

bot = Client(intents=Intents.DEFAULT)

@listen()
async def on_ready():
    print("Baiheng's ready!")

@listen()
async def on_message_create(event):
    print(f"Message received: {event.message.content}")

bot.start(f"{token_1.token_}",status=Status.IDLE)

