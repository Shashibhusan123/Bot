import os
import discord
from discord.ext import commands
from discord import app_commands
import aiohttp

MY_GUILD = discord.Object(id=908715800070877226)

Token = 'OTY4NzU5NDgzMDc5NzQ1NTc2.GS1amY.5oyTaGFw_9Rs6YDysewk4O7tn7EhhYzLKgmRK8'

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$',intents=discord.Intents.all(),application_id=908715800070877226)
        self.synced = False
        #self.tree = app_commands.CommandTree(self)



    async def setup_hook(self):
        for fn in os.listdir('./cogs'):
            if fn.endswith('.py'):
                await bot.load_extension('cogs.{}'.format(fn[:-3]))
            await bot.tree.sync(guild= discord.Object(id=908715800070877226))

    async def close(self):
        await super().close()
        await self.session.close()

    async def on_ready(self):
        print(f'{self.user} is online!')

# bot = MyBot()
# bot.run(Token)
    # logging.basicConfig(level=logging.INFO)
        async with aiohttp.ClientSession() as ahttp, \
               asyncpg.create_pool(...) as db_pool:
                    client = discord.Client()
                    client.ahttp = ahttp
                    client.db_pool = db_pool
                    await client.start(Token)
asyncio.run(main())