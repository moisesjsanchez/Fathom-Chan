import discord
from discord.ext import commands
import os

# initialization
client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')  # ensure extension does not load .py.py

client.run(os.environ['TOKEN'])
