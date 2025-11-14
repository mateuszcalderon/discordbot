# Main settings and commands for the Discord bot.

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from typing import cast

# Load environment variable from .env file.
load_dotenv()
TOKEN = cast(str, os.getenv("DISCORD_TOKEN"))   # Try to fetch the bot token from .env file.

# Error handling for missing environment variable.
if TOKEN is None:
  raise RuntimeError("DISCORD_TOKEN environment variable NOT found.")
else:
  print("DISCORD_TOKEN found. No environment variable issues detected.")

# Define the bot class inheriting from 'commands.Bot'.
class DaVinci(commands.Bot):
    def __init__(self):
      intents = discord.Intents.all()   # Enable all intents.
      super().__init__(command_prefix="/", intents=intents)   # Set the command prefix to '/'.

    async def setup_hook(self):
       # await self.load_extension("cogs.commands")
       await self.load_extension("cogs.events")
       await self.tree.sync()

    async def on_ready(self):
      await self.change_presence(
        activity=discord.Game("github.com/mateuszcalderon"),
        status=discord.Status.online
      )
      print(f"{self.user} bot is ready and running.")

# Instantiate the bot.
bot = DaVinci()

# Write the '@bot.event' down here if something goes wrong with the cogs.

@bot.tree.command(name="emoji", description="Click the button to get a random emoji.")
async def click_me(interaction: discord.Interaction):
  emojis = ["😂", "🥰", "😍", "🤨", "😔", "😴", "🤠", "💀", "🗿"]

  async def button_callback(interaction: discord.Interaction):
    chosen_emoji = random.choice(emojis)
    await interaction.response.send_message(f"{chosen_emoji}")

  view = discord.ui.View()
  button = discord.ui.Button(label="Click me!", style=discord.ButtonStyle.blurple)
  button.callback = button_callback
  view.add_item(button)
  await interaction.response.send_message(
    content="Click the button below to receive a random emoji.",
    view=view
    )

@bot.tree.command(name="ship", description="Find out how much love is between two users.")
async def ship(ctx, user1: discord.Member, user2: discord.Member):
  love_percent = random.randint(0, 100)
  filled = "❤️" * (love_percent // 10)
  empty = "🖤" * (10 - love_percent // 10)
  love_bar = f"[{filled}{empty}]"

  # Generate Love Bar.
  message = (
    f"{user1.mention} x {user2.mention}\n"
    f"Love Percentage: {love_percent}%\n"
    f"{love_bar}"
  )
  await ctx.response.send_message(message)

@bot.tree.command(name="ping", description="Check the bot's latency.")
async def get_ping(interaction: discord.Interaction):
   latency = round(bot.latency * 1000)
   await interaction.response.send_message(f"🛰️ Latency (ms): {latency}")

@bot.tree.command(name="dice", description="Roll a six-sided dice.")
async def roll_dice(interaction: discord.Interaction):
   roll = random.randint(1, 6)
   await interaction.response.send_message(f"🎲 Number: {roll}")

bot.run(TOKEN)
