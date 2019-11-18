import discord
from discord.ext import commands
import asyncio
from itertools import cycle

class Fetch(commands.Cog):

    def __init__(self, client, status):
        self.client = client
        self.status = status
    
    #events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
        print('Bot is online')

    #commands
    @commands.command()
    async def playing(self,ctx):
        await ctx.send('Here are the movies currently known!')
        

def setup(client): 
    client.add_cog(Fetch(client))