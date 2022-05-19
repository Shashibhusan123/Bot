import nextcord
from nextcord.ext import commands
import os
import nextmusic
from nextmusic.ext import Intents

bot = commands.Bot(command_prefix = '$', help_command=None, intents=Intents().intents, case_insensitive=True)

Token = "OTY4NzU5NDgzMDc5NzQ1NTc2.GU3yYk.YRimJcnjU9JeMa-0jKwFk5OnjM8EmPw509krDs"

@bot.event
async def on_ready():
    print('Bot is online')

bot.lavalink_nodes = [
    {
        "host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"
    },
]


bot.load_extension('nextmusic')
bot.run(Token)