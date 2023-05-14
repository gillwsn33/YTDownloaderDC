import discord
import youtube_dl

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('!download'):
        url = message.content.split(' ')[1]
        await download_video(message, url)

async def download_video(message, url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', None)
        video_url = info.get('url', None)

        if title and video_url:
            await message.channel.send(f"Downloading video: {title}")
            ydl.download([url])
            await message.channel.send(f"Video downloaded: {title}")
        else:
            await message.channel.send("Error: Video information not found.")

client.run('MTEwNzEwNzc5MjAyNTgyOTQ1Ng.Gy8Sfj.0nUoflwGPDUKaVFlbcbJkEN3t_Tr7vZJyILgCI')
