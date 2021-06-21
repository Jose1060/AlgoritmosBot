from posix import listdir
import discord
from discord import channel
from discord.activity import Game
from discord.enums import try_enum
from discord.ext import commands
from discord.player import FFmpegAudio
from discord.utils import get
import librerias.Libreria_lista as list

import DiscordUtils


TOKEN = 'ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4'

bot = commands.Bot(command_prefix = '!')

music = DiscordUtils.Music()


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=Game('postmygame.com'))
    print('Bot Ready')

@bot.command(pass_context= True)
async def join(ctx):
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
async def leave(ctx):
    canal = ctx.message.author.voice.channel
    voz = get(bot.voice_clients, guild = ctx.guild)
    await voz.disconnect()


@bot.command(pass_context= True)
async def play(ctx, *, url:str):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    
    if not ctx.voice_client.is_playing():
        await player.queue(url,search=True)
        song = await player.play()
        await ctx.send(f"Empezo a sonar `{song.name}`")

    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"'{song.name}'' fue agregada a la lista")

@bot.command(pass_context=True)
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f" `{',' . join([song.name for song in player.current_queue()])}`")

@bot.command(pass_context= True)
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused `{song.name}`")

@bot.command(pass_context= True)
async def resumen(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed:  `{song.name}`")

@bot.command(pass_context= True)
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(f"Estas escuchando: `{song.name}`")

@bot.command(pass_context= True)
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Omitido : `{data[0].name}`. Sonando ahora: `{data[1].name}`")
    else:
        await ctx.send(f"Omitido :  `{data[0].name}`")

@bot.command(pass_context= True)
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Volumen cambiado de `{song.name}` a `{volume*100}%`")

@bot.command(pass_context= True)
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removido `{song.name}` de la cola")

@bot.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Loop activado: `{song.name}`")
    else:
        await ctx.send(f"Loop desactivado `{song.name}`")

@bot.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")


bot.run(TOKEN)