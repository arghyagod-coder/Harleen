import discord # Discord API
from discord.ext import commands
import youtube_dl # Lib. for handling youtube data extraction
from te import yturl
"""
pip install discord.py
pip install youtube_dl
"""

command_list = """
Here is a list of what can I do: \n
>>> **join**: Before you can play some music you will need to add me to your voice channel, do that by typing `@join` in the chat.
**disconnect**: To turn me off the channel you just simply type `@disconnect` at the chat.
**play**: Finally, to play some music and have fun just type `@play [youtube url]` in the chat.
**pause**: To pause the music now playing type `@pause` in chat.")
**resume**: To unpause/resume the paused music type `@resume` in chat.
"""

class music(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def commandlist(self, ctx):
    await ctx.send(command_list)

  @commands.command()
  async def join(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("You're not in a voice channel. Please enter one.")
    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.mote_to(voice_channel)
  
  @commands.command()
  async def disconnect(self, ctx):
    await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self, ctx, url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
    YDL_OPTIONS = {'format':'bestaudio'}
    vc = ctx.voice_client
    url, title, thumb = yturl(url)
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
      em = discord.Embed(title = f"Playing {title}", color=discord.Color.from_rgb(0, 255, 255))
      em.set_image(url=thumb)
      await ctx.send(embed=em)
  @commands.command()
  async def playurl(self, ctx, url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
    YDL_OPTIONS = {'format':'bestaudio'}
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
    #   em = discord.Embed(title = f"Playing {title}", color=discord.Color.from_rgb(0, 255, 255))
    #   em.set_image(url=thumb)
    #   await ctx.send(embed=em)
  @commands.command()
  async def pause(self, ctx):
    await ctx.voice_client.pause()
    await ctx.send("Paused")

  @commands.command()
  async def resume(self, ctx):
    await ctx.voice_client.resume()
    await ctx.send("Resume")


def setup(client):
  client.add_cog(music(client))