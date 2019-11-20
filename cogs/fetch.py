import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#connecting to Google Sheets API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Anime Movie Showing").sheet1
data = sheet.get_all_records()

#forming one large string to be sent once
movies = 'Here are the weeb movies currently being played near us in the next few months!\n ---------------------------------------------------------------------------------------\n'
repeat_item = []
for item in data:
    movies += (f'{item["Movie Title"]} is being aired on {item["Showing Date"]}.\n')
    #repeat_item = item this for checking for duplicates

class Fetch(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #check if bot is online at time of deployment
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Just chillin drinking boba.'))
        print('Bot is online')

    #manual command to fetch from the current sheet 
    @commands.command()
    async def movie(self,ctx):
        await ctx.send(movies)
        
def setup(client): 
    client.add_cog(Fetch(client))