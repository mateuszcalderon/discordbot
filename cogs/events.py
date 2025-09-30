import discord
from discord.ext import commands
import datetime

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        discord_rgb = discord.Color.from_rgb(114, 137, 218)

        embed = discord.Embed(
            color=discord_rgb,
            title="Welcome!",
            description=f"Welcome to the server, {member.mention}!",
            timestamp=datetime.datetime.now()
        )
        channel = discord.utils.get(member.guild.text_channels, name='welcome')
        if channel:
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        discord_rgb = discord.Color.from_rgb(114, 137, 218)

        embed = discord.Embed(
        color=discord_rgb,
        title="Goodbye!",
        description=f"{member.mention} has left the server.",
        timestamp=datetime.datetime.now()
        )
        channel = discord.utils.get(member.guild.text_channels, name='welcome')
        if channel:
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        discord_rgb = discord.Color.from_rgb(114, 137, 218)

        embed = discord.Embed(
            color=discord_rgb,
            title=f"{channel.name}",
            description=f"A new channel has been created!",
            timestamp=datetime.datetime.now()
        )
        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(EventsCog(bot))