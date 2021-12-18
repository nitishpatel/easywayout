import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import File
import requests

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    activity = discord.Game(name='>your exams are easy')
    await bot.change_presence(activity=discord.Activity(name='>your exams are easy', type=discord.ActivityType.playing))
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def whoami(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send('You are an admin {0.author.mention}'.format(ctx.message))
    else:
        await ctx.send('You are an average joe {0.author.mention}'.format(ctx.message))

@bot.command()
async def getanswer(ctx, id):
    url = f'https://retoolapi.dev/OVxP84/data/{id}'
    response = requests.get(url)
    data = response.json()
    answer = data['Answers']
    question = data['Question']
    await ctx.send(f'Question {question} \nAnswer {answer}')



bot.run(TOKEN)