import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#connecting to Google Sheets API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Anime Movie Showing").sheet1
data = sheet.get_all_records()

class Fetch(commands.Cog):

    def __init__(self, client, status):
        self.client = client
        self.status = status
 
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
        print('Bot is online')

    @commands.command()
    async def playing(self,ctx):
        await ctx.send('Here are the movies currently known!')        

def setup(client): 
    client.add_cog(Fetch(client))