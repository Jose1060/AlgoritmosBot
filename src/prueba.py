from posix import listdir
import discord
from discord import channel
from discord.activity import Game
from discord.enums import try_enum
from discord.ext import commands
from discord.player import FFmpegAudio
from discord.utils import get
import youtube_dl
import os
import librerias.Libreria_lista as list
import shutil


TOKEN = 'ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4'

bot = commands.Bot(command_prefix = '!')

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
    def revisar_lista():
        voice = get(bot.voice_clients, guild = ctx.guild)
        LR_en_archivo = os.path.isdir("./Lista")
        if LR_en_archivo is True:
            DIR = os.path.abspath(os.path.realpath("Lista"))
            tamaño = len(os.listdir(DIR))
            C_Activa = tamaño-1
            try:
                C_primera = os.listdir(DIR)[0]
            except:
                print("No hay Canciones\n")
                listar.clear
            localizacion_principal = os.path.dirname(os.path.realpath(__file__))
            C_localizacion = os.path.abspath(os.path.realpath("Lista") + "\\" + C_primera)  
            if tamaño != 0:
                print("Cancion Lista, se reproducira en breve")
                print(f" canciones en la lista: {C_Activa}")
                C_Encontrada = os.path.esfile("cancion.mp3")
                if C_Encontrada:
                    os.remove("cancion.mp3")
                    shutil.move(C_localizacion, localizacion_principal)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, "cancion.mp3")
                    
                    voice.play(discord.FFmpegPCMAudio("cancion.mp3"), after = lambda e: revisar_lista())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.06
                else:
                    listar.clear()
                    return

        else:
            print("No se agrego la cancion a la lista")

    C_Encontrada = os.path.isfile("cancion.mp3")
    try:
        if C_Encontrada:
            os.remove("cancion.mp3")
            listar.clear()
            print("removido archivo antiguo")
    
    except PermissionError:
        print("se ha intentado eliminar un archivo, pero este se encuentra Reproduciendo")
        await ctx.send("ERROR: Cancion reproduciendo")
        return
    
    LR_en_archivo = os.path.isdir("./Lista")
    try:
        LR_Carpeta = "./Lista"
        if LR_en_archivo is True:
            print("removida la carpeta antigua")
            shutil.rmtree(LR_Carpeta)

    except:
        print("No hay carpeta antigua")

    await ctx.send("Todo listo")
    voice = get(bot.voice_clients, guild = ctx.guild)

    ydl_opciones = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opciones) as ydl:
        print("Descargando Cancion\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renombrando el archivo: {file}\n")
            os.rename(file, "cancion.mp3")
    
    voice.play(discord.FFmpegPCMAudio("cancion.mp3"), after= lambda e: revisar_lista())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.06

    nombre = name.rsplit("-",2)
    await ctx.send(f"**Reproduciendo: ** {nombre[0]}")
    print("Reproduciendo \n")





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

#listar = list.LinkedList()
listar = {}

@bot.command(pass_context= True)
async def lista(ctx, url:str):
    cancion_lista = os.path.isdir("./Lista")
    if cancion_lista is False:
        os.mkdir("Lista")
    dir = os.path.abspath(os.path.realpath("Lista"))
    Lista_num = len(os.listdir(dir))
    Lista_num += 1
    Agregar_Lista = True
    while Agregar_Lista:
        if Lista_num in listar:
            Lista_num =+ 1
        else:
            Agregar_Lista = False
            listar[Lista_num] = Lista_num

    Lista_path = os.path.abspath(os.path.realpath("Lista")+ f"\cancion{Lista_num}.%(ext)s") 

    ydl_opciones = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': Lista_path,
        'postprocessors' : [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opciones) as ydl:
        print("Descargar Cancion")
        ydl.download([url])
    await ctx.send("Añadida la cancion" + str(Lista_num) +"a la lista de reproduccion")

    print("Cancion añadida")


bot.run(TOKEN)