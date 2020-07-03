import discord
import random
import youtube_dl
from discord.ext import commands as cm
from discord.utils import get
TOKEN = ${{secrets.DISCORD_TOKEN}}

client = cm.Bot(command_prefix='!')
@client.event
async def on_ready():
    print('BOT Подключен!')


@client.command()
async def hello(ctx):
    hello_list = ['Здарова, Тварына',
                  'Ну привет',
                  "Здарова, работяги",
                  "Привет трудящимся!",
                  "Привет",
                  "Нормально, че",
                  "Найс начало, сцуко",
                  "Ку бойцам!",
                  "А вы все думали, когда же я появлюсь...",
                  'Каждый сука раз одно и то же',
                  'В СОЛЯНОВА!',
                  'Подрубочка',
                  'Лимончик',
                  'Здарова',
                  'Як Справы',
                  'Як Справы, работяги',
                  'Да Да Я',
                  'Здоровеньки булы',
                  'Швыдче, хлопцы, Швыдче',
                  'Доброго времени бытия']
    await ctx.send(random.choice(hello_list))

command_list = ['!hello - поприветствовать тебя\n',
                '!ping - сыграть в пинг-понг\n',
                '!gachi - высрать рандомную гачи фразу\n',
                '!goass - послать тебя в жопу\n',
                '!DDOS - ЖОПА минус чат\n']


@client.command(pass_context=True)
async def goass(cxt):
    author = cxt.message.author
    fuck_you_list = [' Да иди ты на хер',
                     ' Ты дуранчеус',
                     ' Лол чел ты в муте',
                     ' Соси ногу',
                     ' Жопу сосал?',
                     ' Fuck you',
                     ' Иди в жопу']
    await cxt.send(f'{author.mention}' + random.choice(fuck_you_list))


@client.command()
async def DDOS(ext):
    author = ext.message.author
    while(True):
        await ext.send(f'{author.mention} вызвал ДУДОС')


@client.command()
async def commands(ctx):
    global command_list
    await ctx.send('Вот что я могу:\n')
    for i in command_list:
        await ctx.send(i)


@client.command()
async def gachi(ctx):
    gachi_list = ['Let Celebrate and Suck some Dicks',
                  'Hey Bro! Nice Dick!',
                  'Fuck Yoouuuu',
                  'Huh You like Embarrasing me Huh?',
                  "Oh Shit, i'm Sorry",
                  'Swallow my Cum',
                  'Fuck you Leatherman']
    await ctx.send(random.choice(gachi_list))


@client.command()
async def ping(ctx, txt):
    await ctx.send('@everyone\n' + txt)


@client.command()
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)


@client.command()
async def gay_is(ctx, member: discord.Member):
    await ctx.send('Gay')




#class MyClient(discord.Client):
#    async def on_ready(self):
#        print('Logged on as {0}!'.format(self.user))


#    async def on_message(self, message):
 #       print('Message from {0.author}: {0.content}'.format(message))


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    try:
        await channel.connect()
    except:
        await ctx.send('Зайди в голосовой канал, дурачок')
        return


@client.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

import os
bot = cm.Bot(command_prefix='!')
@client.command(pass_context=True)
async def play(ctx, url:str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ("Сейчас играет музыка")
        return

    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith('.mp3'):
            name = file
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegAudio("song.mp3"), after=lambda e:print(f"{name} finished playing"))

    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.40

    nname = name.split("-", 2)
    await ctx.send(f"Playing{nname}")
#async def play(ctx, url):

##    if not client.is_voice_connected(ctx.message.server):
 #       voice = await client.join_voice_channel(ctx.message.author.voice_channel)
 #   else:
 #       voice = client.voice_client_in(ctx.message.server)

  #  player = await voice.create_ytdl_player(url, after=toggle_next)
   # await songs.put(player)

client.run(TOKEN)
