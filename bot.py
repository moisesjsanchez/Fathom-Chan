import discord
from discord.ext import commands
import crontab
import os

token = 'NjQ1MjAyNDQ4NzA0ODY0MjU3.Xc_JxA.WleytSNTz-hJfAt5_-Z0I0XPW4c'
client = commands.Bot(command_prefix = '.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') #to fix loadings .py.py

client.run(token) 
