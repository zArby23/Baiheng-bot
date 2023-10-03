from interactions import Client, Intents, Status, listen
from interactions.api.events import MessageCreate
import token_1

bot = Client(intents=Intents.DEFAULT,
             activity="WIP")

@listen()
async def on_ready():
    print("Baiheng's ready!")

bot.load_extension("Commands.ping")
bot.reload_extension("Commands.ping")
bot.start(f"{token_1.token_}")

