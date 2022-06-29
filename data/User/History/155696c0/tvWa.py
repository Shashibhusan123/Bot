import discord, config
from discord.ext import commands
from discord import app_commands
from config import TOKEN


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ready = False