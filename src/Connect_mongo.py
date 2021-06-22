import discord
import pymongo
from discord import channel
from discord.activity import Game
from discord.enums import try_enum
from discord.ext import commands
from discord.player import FFmpegAudio
from discord.utils import get
import librerias.Libreria_lista as list

import DiscordUtils



client = pymongo.MongoClient("mongodb+srv://admin:DSTecsup2@cluster0.m9azk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
TOKEN = 'ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4'

bot = commands.Bot(command_prefix = '!')

"""
for database_name in client.list_database_names():  
    print("Database - "+database_name)  
    for collection_name in client.get_database(database_name).list_collection_names():  
        print(collection_name)  
"""

print('Find One document')  
print(client.PostMyGame.news.find_one())  

print('Find all documents')  
for x in client.PostMyGame.news.find():  
    print("="*80)
    print(x, "\n")  

print('Find documents with condition')  
for x in client.PostMyGame.news.find({"title": "Ad commodi id enim nisi."}):  
    print("="*80)
    print(x)  



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=Game('postmygame.com'))
    print('Bot Ready')



bot.run(TOKEN)