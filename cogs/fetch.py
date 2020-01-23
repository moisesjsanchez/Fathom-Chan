import discord
from discord.ext import commands
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# connecting to Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(os.environ.get('CREDS')), scope)
client = gspread.authorize(creds)
sheet = client.open("Anime Movie Showing").sheet1
data = sheet.get_all_records()

# forming one large string to be sent once
movies = 'Here are the weeb movies currently being played near us in the next few months!\n ---------------------------------------------------------------------------------------'
repeat_item = {"Movie Title": '', "Showing Data": ''}  # initial dictonary value for matching
for item in data:
    if repeat_item["Movie Title"] == item["Movie Title"]:
        movies += (f' and {item["Showing Date"]}')
    else:
        movies += (f'\n{item["Movie Title"]} is being aired on {item["Showing Date"]}')
    repeat_item = item


class Fetch(commands.Cog):

    def __init__(self, client):
        self.client = client

    # check if bot is online at time of deployment
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('For help use .help command mang'))
        print('Bot is online')

    # manual command to fetch from the current sheet
    @commands.command()
    async def movies(self, ctx):
        await ctx.send(movies)


def setup(client):
    client.add_cog(Fetch(client))
