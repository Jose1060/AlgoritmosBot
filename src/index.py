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

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


bot = commands.Bot(command_prefix='~P ', description='Este bot es de PostMyGames')

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

@bot.command( help ='Este comando reproduce musica')
async def play(ctx, url : str):
    """
    VoiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Sala')
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await VoiceChannel.connect()
    """
    if not ctx.message.author.voice:
        await ctx.send('No estas conectado a un canal de voz')
        return
    else:
        channel = ctx.message.author.voice.channel

    async with ctx.typing():
        playlist = list.LinkedList()
        if playlist.length == 0:
            print ("estas en el if lenght = 0",playlist.length)
            await channel.connect()

            server = ctx.message.guild
            voice_channel = server.voice_client

            player = await YTDLSource.from_url(url, loop = bot.loop)
            playlist.insertAtBegin(player)
            playlist.print()
            voice_channel.play(playlist.head.data, after=lambda e: print('Player error: %s' %e)if e else None)
            await ctx.send(f'**Now playing:** {playlist.head.data.title}')
            print (playlist.length)

        elif playlist.length > 0:
            print ("estas en el if lenght > 0",playlist.length)
            server = ctx.message.guild
            voice_channel = server.voice_client

            
            player = await YTDLSource.from_url(url, loop = bot.loop)
            playlist.insertAtBegin(player)
            playlist.print()
            voice_channel.play(playlist.head.data, after=lambda e: print('Player error: %s' %e)if e else None)
            await ctx.send(f'**Now playing:** {playlist.head.data.title}')

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_connected():
        await voice.disconnected()
    else:
        await ctx.send("El bot no es conectado a un canal de voz")

@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No se reproduce nada")

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("El audio no esta pausado")

@bot.command()
async def stop(ctx):
    """
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    """
    voice = ctx.message.guild.voice_client
    await voice.disconnect()

# Evento
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=Game('postmygame.com'))
    print('Bot Ready')

bot.run('ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4')
