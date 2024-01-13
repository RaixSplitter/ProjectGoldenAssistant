from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
import asyncio

PREFIX = "!"
INTENTS = discord.Intents.all()
class GoldenAssistantBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX, intents=INTENTS)
        
        self.load_commands()

       

    async def on_ready(self):
        print(f"Bot {self.user.display_name} is connected to server.")
        
        
    def load_commands(self) -> None:
        @self.command(name="test")
        async def custom_command(ctx):
            await ctx.send("Hello")


if __name__ == "__main__":
    load_dotenv()
    discord_token = os.getenv("DISCORD_TOKEN")
    bot = GoldenAssistantBot()
    bot.run(discord_token)