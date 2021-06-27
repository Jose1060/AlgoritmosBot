import datetime
from os import name
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
import time
import DiscordUtils
import asyncio



client = pymongo.MongoClient("mongodb+srv://admin:DSTecsup2@cluster0.m9azk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
TOKEN = 'ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4'

bot = commands.Bot(command_prefix = '--')

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


def Noticias_all():
    noticias = list.LinkedList()
    for i in client.PostMyGame.news.find():
        if noticias.length == 0:
            noticias.insertAtBegin(i)
        elif noticias.length > 0:
            noticias.insertAtEnd(i)
    #noticias.print()
    return noticias

def Noticias_day():
    noticias = list.LinkedList()
    date1 = datetime.datetime.now()
    # creamos una variable con 1 dia
    dia = datetime.timedelta(days=1)
    date1 = date1 - dia
    print(date1)

    for i in client.PostMyGame.news.find():
        date = i['created_at']
        if date > date1:
            if noticias.length == 0:
                    noticias.insertAtBegin(i)
            elif noticias.length > 0:
                noticias.insertAtEnd(i)

    #noticias.print()
    return noticias

def msg_embed(noticia):
    noticia_tmp = noticia

    embed = discord.Embed(title=f"{noticia_tmp.data['title']}", description=f"{noticia_tmp.data['content']}", timestamp=noticia_tmp.data['updated_at'],color=discord.Color.blue())        
    user = client.PostMyGame.users.find_one({"_id": ObjectId(noticia_tmp.data['user_id'])})
    embed.set_author(name = "postmygames.tk", icon_url = bot.user.avatar_url, url = "https://postmygames.tk/new/" + str(noticia_tmp.data['_id'])) 
    embed.set_image(url = "https://c0.klipartz.com/pngpicture/603/654/gratis-png-portal-2-laboratorios-de-vida-media-apertura-logo-portal.png")

    embed.set_footer(icon_url = "https://c0.klipartz.com/pngpicture/603/654/gratis-png-portal-2-laboratorios-de-vida-media-apertura-logo-portal.png", text = f"Publicado por{user['name']}")
    
    embed.set_thumbnail(url="https://c0.klipartz.com/pngpicture/603/654/gratis-png-portal-2-laboratorios-de-vida-media-apertura-logo-portal.png")
    return(embed)
    


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=Game('postmygame.com'))
    print('Bot Ready')
    DiscordComponents(bot)


@bot.command()
async def noticias(ctx):
    # Embed 1 para las noticias del dia
    one = Button(style=ButtonStyle.grey, label="Ver todas las noticias", id="todas_noticias")
    two = Button(style=ButtonStyle.blue, label="Ver noticias del dia", id="dia_noticias")
    three = Button(style=ButtonStyle.red, label="Exit", id="exit")
    next = Button(style=ButtonStyle.blue, label="next", id="next")
    exit = Button(style=ButtonStyle.blue, label="exit", id="exit")

    opciones = await ctx.send(
        "Noticias",
        components=[
            [
                one,
                two,
                three,
            ]
        ]
    )
    
    buttons = {
        "todas_noticias": "op1",
        "dia_noticias": "op2",
        "exit": "exit",
    }

    while True:
        event = await bot.wait_for("button_click")
        if event.channel is not ctx.channel:
            return
        if event.channel == ctx.channel:
            response = buttons.get(event.component.id)
            print(response)
            if response is None:
                await event.channel.send("Oh, algo salido mal, porfavor intentalo de nuevo")
            if event.channel == ctx.channel:
                if response == "op2":

                    await opciones.delete()

                    noticias_day = Noticias_day()
                    noticia = noticias_day.head
                    embed1 = msg_embed(noticia)
                    noticia_embed = await ctx.send(
                        "Seleccione una opcion",
                        embed = embed1,
                        components=[
                            [
                                next,
                                exit,
                            ]
                        ]
                    )
                    buttons = {
                        "next" : "next",
                        "exit" : "exit",
                    }
                    while True:
                        event = await bot.wait_for("button_click")
                        if event.channel is not ctx.channel:
                            return
                        if event.channel == ctx.channel:
                            response2 = buttons.get(event.component.id)
                            print(response2)
                            if response2 is None:
                                await event.channel.send("Oh, algo salido mal, porfavor intentalo de nuevo")
                            if event.channel == ctx.channel:
                                if response2 == "next":
                                    await noticia_embed.delete()
                                    noticia = noticia.next
                                    embed1 = msg_embed(noticia)
                                    noticia_embed = await ctx.send(
                                    "Seleccione una opcion",
                                    embed = embed1,
                                    components=[
                                        [
                                            next,
                                            exit,
                                        ]
                                    ]
                                    )
                                    buttons = {
                                        "next" : "next",
                                        "exit" : "exit",
                                    }        
                                if response2 == "exit":
                                    noticias_day.clear()
                                    await noticia_embed.delete()

                                    embed = discord.Embed(title=f"Bye", description="Si desea volver a usar la funcion de noticias solo tienes que usar `--noticias`", timestamp= datetime.datetime.now(),color=discord.Color.blue()) 
                                    embed.set_author(name = "postmygames.tk", icon_url = bot.user.avatar_url, url = "https://postmygames.tk/" ) 
                                    embed.set_footer(icon_url = bot.user.avatar_url, text = "Bye")

                                    msg_fin = await ctx.send(embed = embed)
                                    await asyncio.sleep(40) # waiting 60 seconds
                                    await msg_fin.delete()
                                    break

                if response == "op1":

                    await opciones.delete()

                    noticias_day = Noticias_all()
                    noticia = noticias_day.head
                    embed1 = msg_embed(noticia)
                    noticia_embed = await ctx.send(
                        "Seleccione una opcion",
                        embed = embed1,
                        components=[
                            [
                                next,
                                exit,
                            ]
                        ]
                    )
                    buttons = {
                        "next" : "next",
                        "exit" : "exit",
                    }
                    while True:
                        event = await bot.wait_for("button_click")
                        if event.channel is not ctx.channel:
                            return
                        if event.channel == ctx.channel:
                            response2 = buttons.get(event.component.id)
                            print(response2)
                            if response2 is None:
                                await event.channel.send("Oh, algo salido mal, porfavor intentalo de nuevo")
                            if event.channel == ctx.channel:
                                if response2 == "next":
                                    await noticia_embed.delete()
                                    noticia = noticia.next
                                    embed1 = msg_embed(noticia)
                                    noticia_embed = await ctx.send(
                                    "Seleccione una opcion",
                                    embed = embed1,
                                    components=[
                                        [
                                            next,
                                            exit,
                                        ]
                                    ]
                                    )
                                    buttons = {
                                        "next" : "next",
                                        "exit" : "exit",
                                    }        
                                if response2 == "exit":
                                    noticias_day.clear()
                                    await noticia_embed.delete()

                                    embed = discord.Embed(title=f"Bye", description="Si desea volver a usar la funcion de noticias solo tienes que usar `--noticias`", timestamp= datetime.datetime.now(),color=discord.Color.blue()) 
                                    embed.set_author(name = "postmygames.tk", icon_url = bot.user.avatar_url, url = "https://postmygames.tk/" ) 
                                    embed.set_footer(icon_url = bot.user.avatar_url, text = "Bye")

                                    msg_fin = await ctx.send(embed = embed)
                                    await asyncio.sleep(40) # waiting 60 seconds
                                    await msg_fin.delete()
                                    break
                if response == "exit":

                    await opciones.delete()

                    embed = discord.Embed(title=f"Bye", description="Si desea volver a usar la funcion de noticias solo tienes que usar `--noticias`", timestamp= datetime.datetime.now(),color=discord.Color.blue()) 
                    embed.set_author(name = "postmygames.tk", icon_url = bot.user.avatar_url, url = "https://postmygames.tk/" ) 
                    embed.set_footer(icon_url = bot.user.avatar_url, text = "Bye")
                    msg_fin = await ctx.send(embed = embed)
                    await asyncio.sleep(40) # waiting 60 seconds
                    await msg_fin.delete()
                    break

        break

bot.run(TOKEN)