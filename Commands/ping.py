from interactions import slash_command, SlashContext, Extension
import time

class ping(Extension):
    @slash_command(name="ping",description="Test your ping to the bot!")
    async def ping(self, ctx: SlashContext):
        start_time = time.time()
        await ctx.defer()
        end_time = time.time()
        elapsed_time_seconds = round((end_time - start_time), 2)
        await ctx.send(f"Elapsed time: {elapsed_time_seconds} seconds.")

def setup(bot):
    ping(bot)