import discord
from discord.ext import commands

class Help(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #settings up the custom help functions 
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = 'Fathom Chan', description = "A bot for your Fathom anime film related needs. Below are a list of commands:", color = 0xE69138)

        embed.add_field(name = '.help', value = 'Calls up list of commands that user can perform', inline = False)
        embed.add_field(name = '.movies', value = 'Fetchs current Fathom event anime movies playing', inline = False)
        embed.add_field(name = '.reminder X', value = 'Sets up a reminder that goes off the day before **X** movie plays', inline = False)
        embed.add_field(name = '.refresh_on', value = 'Enables bot to automatic display what movies are playing on a monthly basis', inline = False)
        embed.add_field(name = '.refresh_off', value = 'Disables automatic monthly movie messages', inline = False)

        await ctx.send(embed = embed)
    
def setup(client):
    client.add_cog(Help(client))