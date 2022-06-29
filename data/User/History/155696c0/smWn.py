import discord, config
from discord.ext import commands
from discord import app_commands
from config import TOKEN


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ready = False



    async def on_ready(self):
        if not self.ready:
            print(f'----------------------------')
            print(f'Client is ready as {self.user}')
            print(f'----------------------------')

bot = Bot()