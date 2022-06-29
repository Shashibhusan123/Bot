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

bot = Bot(command_prefix='$',
         help_command=None,
        case_insencitive=True,
        intents=discord.Intents.default(), activity=discord.Activity(type=discord.ActivityType.listening, name='Self laga dunga', status=discord.Status.idle))


async def main():
    for fn in os.listdir('Cogs'):
        if fn.endswith('.py'):
            await bot.load_extension(f'Cogs.{fn[:-3]}')

    async with bot:
        await bot.start(token=TOKEN, reconnect=True)
        
