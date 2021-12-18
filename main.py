import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import File

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    activity = discord.Game(name='>your exams are easy')
    await bot.change_presence(activity=discord.Activity(name='>your exams are easy', type=discord.ActivityType.watching))
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)