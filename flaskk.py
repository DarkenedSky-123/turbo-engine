import discord
from discord.ext import commands
from moviepy.editor import *

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("/rynx"))
    print("Bot is Ready")

@bot.tree.command(name="hello", description="Says hello to you!")
async def hello(interaction: discord.Interaction):
    greeting = f"Hello, {interaction.user.name}! "  # Use interaction.user.name for personalization
    await interaction.response.send_message(greeting, ephemeral=False) 

    # Create a 3-second video with MoviePy
    black_clip = ColorClip(size=(1920, 1080), color=[0, 0, 0], duration=3)

    # Write the clip to a file
    black_clip.write_videofile("black_screen.mp4", fps=24)

    # Send the video file to the channel
    with open("black_screen.mp4", "rb") as file:
        await interaction.channel.send(file=discord.File(file, filename="black_screen.mp4"))

bot.run('')
