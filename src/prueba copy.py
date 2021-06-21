import discord
from discord import channel
from discord.activity import Game
from discord.ext import commands
from discord.player import FFmpegAudio
from discord.utils import get
import youtube_dl
import os
import librerias.Libreria_lista

TOKEN = 'ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4'

bot = commands.Bot(command_prefix = '$pn')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=Game('postmygame.com'))
    print('Bot Ready')

@bot.command(pass_context= True)
async def conectar(ctx):
    canal = ctx.message.author.voice.channel
    if not canal:
        await ctx.send("No estas conectado a un canal")
        return
    voz = get(bot.voice_clients,guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    
    else:
        voz = await canal.connect()

@bot.command(pass_context= True)
async def desconectar(ctx):
    canal = ctx.message.author.voice.channel
    voz = get(bot.voice_clients, guild = ctx.guild)
    await voz.disconnect()

@bot.command(pass_context= True)
async def play(ctx, url:str):
    cancion_activa = os.path.isfile("cancion.mp3")
    try:
        if cancion_activa:
            os.remove("cancion.mp3")
            print("la cancion se removio")
    except PermissionError:
        print ("hay una cancion reproduciendose")
        await ctx.send("Error: cancion reproduciendose")
        return
    await ctx.send("Todo listo")

    voz = get(bot.voice_clients, guild = ctx.guild)

    ydl_opciones = {
        'format': 'bestaudio/best',
        'postprocessors' : [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }],
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

    with youtube_dl.YoutubeDL(ydl_opciones) as ydl:
        print("Descargar Cancion", url)
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renombramos Archivo: {file}")
            os.rename(file, "cancion.mp3")
    
    voz.play(discord.FFmpegPCMAudio("cancion.mp3"), after= lambda e: print("Termino"))
    voz.source = discord.PCMVolumeTransformer(voz.source)
    voz.source.volume = 0.06

    nombre = name.rsplit("-",2)
    await ctx.send(f"**Reproduciendo**: {nombre[0]}" )

@bot.command(pass_context=True)
async def pausa(ctx):
    voz = get(bot.voice_clients, guild = ctx.guild)
    if voz and voz.is_playing():
        print("Musica Pausada")
        voz.pause()
        await ctx.send("Musica Pausada")
    else:
        print("No se esta reproduciendo nada")
        await ctx.send("No se esta reproduciendo nada")

@bot.command(pass_context= True)
async def resumen(ctx):
    voz = get(bot.voice_clients, guild = ctx.guild)
    if voz and voz.is_paused():
        print("Musica reanudada")
        voz.resume()
        await ctx.send("Musica Reanudada")
    else:
        print("La musica no esta pusada")
        await ctx.send("No se escuentra pausada")

@bot.command(pass_context= True)
async def detener(ctx):
    voz = get(bot.voice_clients, guild = ctx.guild)
    if voz and voz.is_playing():
        print("Musica detenida")
        voz.stop()
        await ctx.send("Musica Detenida")
    else:
        print("No se esta reproduciendo")
        await ctx.send("No se esta reproduciendo")

bot.run(TOKEN)