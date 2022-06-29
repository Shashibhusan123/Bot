import discord
from discord.ext import commands
from discord import app_commands
# from main import MY_GUILD

class test(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name='ping', description='Bot latency')
    async def ping(self, interaction: discord.Interaction, member: discord.Member, reason=None):
        if reason==None:
            reason="No reason provided"
        await interaction.guild.kick(member)
        await interaction.response.send_message(f'User {member.mention} has been kicked for {reason}')
  


async def setup(bot: commands.Bot):
    await bot.add_cog(test(bot),guilds=[discord.Object(id=908715800070877226)])