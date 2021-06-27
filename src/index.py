import asyncio
import discord
import librerias.Libreria_lista as list
from discord import embeds
from discord import client
from discord import guild
from discord.activity import Game
from discord.channel import VoiceChannel
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands import bot
import datetime
from urllib import parse, request
import re
from discord.voice_client import VoiceClient
from discord.webhook import RequestsWebhookAdapter
import youtube_dl
from random import choice
import Connect_mongo
import Music

bot = commands.Bot(command_prefix='--', description='Este bot es de PostMyGames')

@bot.command()

async def ping(ctx):
    await ctx.send('¡pong! {0}'. format(round(bot.latency, 1)))

@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Este servidor es de la pagina PostMyGames, dode puede disfutar de tus juegos con las demas personas :D!!", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Servidor creado", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del servidor", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del servidor", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://www.senpai.com.mx/wp-content/uploads/2020/04/Naruto_-Este-fanart-nos-muestra-una-versio%CC%81n-realista-de-Itachi-Uchiha.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    
    print('http://www.youtube.com/results?' + query_string)

    """
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    """

    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    #print(search_results)
    await ctx.send('http://www.youtube.com/watch?v=' +search_results[0])


bot.run('ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4')
