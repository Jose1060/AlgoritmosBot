import datetime
from bson.objectid import ObjectId
import discord
from discord.ext.commands.core import check
import pymongo
from discord import channel
from discord.activity import Game
from discord.enums import try_enum
from discord.ext import commands
from discord.player import FFmpegAudio
from discord.utils import get
from discord_components import *
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

# Comandos de busqueda
"""
print('Find One document')  
print(client.PostMyGame.news.find_one())  

print('Find all documents')  
for x in client.PostMyGame.news.find():  
    print("="*80)
    print(x, "\n")  
"""
"""
print('Find documents with condition')  
for x in client.PostMyGame.news.find({"title": "Ad commodi id enim nisi."}):  
    print("="*80)
    print(x)  
"""


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=Game('postmygame.com'))
    print('Bot Ready')
    DiscordComponents(bot)

noticias = list.LinkedList()
@bot.command(pass_context= True)
async def news(ctx):
    for i in client.PostMyGame.news.find():
        noticias.insertAtBegin(i)
        noticias.print()
        embed = discord.Embed(title=f"{noticias.head.data['title']}", description=f"{noticias.head.data['content']}", timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
        
        user = client.PostMyGame.users.find_one({"_id": ObjectId(noticias.head.data['user_id'])})
        print(user)

        embed.add_field(name="Fecha de publicacion", value=noticias.head.data['updated_at'].strftime("%Y-%m-%d %H: %M:%S"))
        embed.add_field(name="Autor", value=user['name'])
        await ctx.send(embed=embed)



@bot.command()
async def button(ctx):
    await ctx.send(
        "This is a Button", components=[Button( style=ButtonStyle.blue, label = 'Click me!')]
    )
    interaction = await bot.wait_for("button_click", check=lambda i: i. component.label.startswith("Click"))

    await interaction.respond(content="Button Clicked!")

bot.run(TOKEN)