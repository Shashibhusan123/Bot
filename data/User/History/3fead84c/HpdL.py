import discord, typing
from typing import Optional
from discord.ext import commands
from discord import app_commands
# from main import MY_GUILD

class test(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name='kick', description='Kick a member')
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]):
        if reason==None:
            reason="No reason provided"
        await interaction.guild.kick(member)
        await interaction.response.send_message(f'User {member.mention} has been kicked for {reason}')


    @commands.hybrid_command(name='ping', guild_ids=[908715800070877226])
    async def ping(self, ctx):
        await ctx.send(embed=discord.Embed(title='My ping', description=f"My ping is {bot.latency * 1000: 2f}mc"))
  


async def setup(bot: commands.Bot):
    await bot.add_cog(test(bot),guilds=[discord.Object(id=908715800070877226)])