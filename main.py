# Imports
from discord.ext import commands
import random
from ext import *
import os # For fetching ENV SECRETS
from keep_alive import keep_alive # Uptime Robot SRC file
import re, urllib.parse, urllib.request
from random import choice
from youtube_search import YoutubeSearch # pip install youtube_search
import time # Sleep functions
import discord # pip install discord.py
import praw # pip install praw
import pyjokes # pip install pyjokes
import googlesearch # pip install beautifulsoup4 google
import requests, json, wikipedia # pip install requests wikipedia
from dotenv import load_dotenv # pip install python-dotenv
from titan import shorten # Shortening urls with titan
import bs4

# ---------------------------------------------------------------------------------------

import music
cogs = [music] 

bot = commands.Bot(command_prefix="h!", intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(bot)

# Fetching environment variables (API keys and private stuff)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 
GUILD = os.getenv('DISCORD_GUILD')
REDDIT_CID = os.getenv('REDDIT_CID')
REDDIT_SCT = os.getenv('REDDIT_SCT')
TKEY = os.getenv("TENOR_KEY")
CBAPI = os.getenv("CBAPI")
prefixes={}
# ---------------------------------------------------------------------------------------
import TenGiphPy
t = TenGiphPy.Tenor(token=TKEY)
# bot = discord.Client()
# Initializing Discord Client
client = discord.Client()

# ---------------------------------------------------------------------------------------

# Initial Prefix
# with open("guilds.json") as f:
#     guild = message.channel.guild
#     x = json.load(f)
#     prefix = x[guild.id]
prefix="h!"

# ---------------------------------------------------------------------------------------

# Function to get memes from praw (Python Reddit API Wrapper)
def getmeme(topic): # Topic/Subreddit name
    reddit = praw.Reddit(client_id=REDDIT_CID,
                    client_secret=REDDIT_SCT,
                    user_agent='meme') # Initializing details

    submission = reddit.subreddit(topic).random()
    return submission.url

# ---------------------------------------------------------------------------------------

# GIFs for Damn Son react
dms = ["https://giphy.com/gifs/batman-film-qVID3J8fLrlZK", "https://giphy.com/gifs/homer-simpson-barney-batman-and-robin-pSFEEQMaNcFAQ", "https://giphy.com/gifs/hug-5sos-5-seconds-of-summer-BcOvvS5t0sxnG", 'https://giphy.com/gifs/joker-the-joaquin-phoenix-A7ZbCuv0fJ0POGucwV']

# GIFs for LOL react
lolm = ['https://giphy.com/gifs/originals-lol-3o6ozvv0zsJskzOCbu', 'https://giphy.com/gifs/theoffice-episode-6-the-office-tv-bC9czlgCMtw4cj8RgH','https://giphy.com/gifs/moodman-lol-spit-take-Q7ozWVYCR0nyW2rvPW', 'https://giphy.com/gifs/moodman-funny-lol-laughing-fUYhyT9IjftxrxJXcE', 'https://giphy.com/gifs/laughing-despicable-me-minions-ZqlvCTNHpqrio', 
'https://giphy.com/gifs/laughing-applause-mike-tyson-wWue0rCDOphOE']

# GIFs for Yay reaction
yaym = [
    "https://giphy.com/gifs/F9hQLAVhWnL56",
    "https://giphy.com/gifs/thegifys-gifys-5xaOcLGvzHxDKjufnLW",
    "https://giphy.com/gifs/studiosoriginals-dog-josh-freydkis-bad-woof-l41Ym8O8dbIG0XvFK",
    "https://giphy.com/gifs/sherlockgnomes-sherlock-l4pTfx2qLszoacZRS",
    'https://giphy.com/gifs/foxinternational-reaction-simpsons-celebrate-26tPplGWjN0xLybiU',
    "https://giphy.com/gifs/excited-screaming-jonah-hill-5GoVLqeAOo6PK",
    "https://giphy.com/gifs/excited-yes-30-rock-I24hjk3H0R8Oc"
]



# GIFs for Yes Reaction
yesm = [
    "https://giphy.com/gifs/theoffice-MNmyTin5qt5LSXirxd",
    "https://giphy.com/gifs/DffShiJ47fPqM",
    "https://giphy.com/gifs/dYZuqJLDVsWMLWyIxJ"
]

susm = ["https://giphy.com/gifs/confused-futurama-suspicious-ANbD1CCdA3iI8","https://giphy.com/gifs/moodman-monkey-side-eye-sideeye-H5C8CevNMbpBqNqFjl","https://giphy.com/gifs/tiktok-cute-aww-jRHD367KLHU7NsPjmb",
"https://giphy.com/gifs/reaction-mood-3gNotAoIRZsb9UHPnj"]

# GIFs for No Reaction
nom = [
    "https://giphy.com/gifs/the-office-mrw-d10dMmzqCYqQ0",
    "https://giphy.com/gifs/NetflixisaJoke-netflix-iglesias-mr-h5cl6eHMvf0IQ3wJch",
    "https://giphy.com/gifs/memecandy-J46T6SB3yzwc4eBYeL"
]

# ---------------------------------------------------------------------------------------

# Use of Zenquotes API to fetch motivating quotes
def get_quote():
    res = requests.get("https://zenquotes.io/api/random")
    jsond= json.loads(res.text)
    quote = jsond[0]['q']
    auth = (jsond[0]['a'])
    return quote, auth

# ---------------------------------------------------------------------------------------

# Use of youtubesearch module to fetch youtube results
def searchyt(song):
    music_name = song
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    return clip2

# ---------------------------------------------------------------------------------------
# @client.event
# async def on_guild_join(guild):
#     dict1 = {guild.id : "h!"}
#     with open("guilds.json", "r+") as fi:
#         data = json.load(fi)
#         data.update(dict1)
#         fi.seek(0)
#         json.dump(data, fi)
 
# Starting success message after Initialization
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# ---------------------------------------------------------------------------------------

# Function to DM people who join the server (unfunctional for now)
@bot.event
async def on_member_join(member):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to {guild.name}!'
    )

# ---------------------------------------------------------------------------------------

# Function executing on a message
@bot.event
async def on_message(message):
    cm = message.content
    if message.author == bot.user:
        return

# ---------------------------------------------------------------------------------------
    
    # Func- Shorten URLs with titanURL 
    if message.content.startswith(f"{prefix}short"):
        queries = (message.content).replace(
            f"{prefix}short", "").lstrip().rstrip().split(" ")
        if len(queries) == 1:
            await message.channel.send(shorten(queries[0]))
        elif len(queries) == 2:
            await message.channel.send(shorten(queries[0], queries[1]))
        elif len(queries) == 3:
            await message.channel.send(shorten(queries[0], queries[1], queries[2]))
        else:
            await message.channel.send("Invalid query! The command syntax is `binod.shorten <url_to_shorten> <alias_type> <alias>`.")
    
# ---------------------------------------------------------------------------------------

    # Help command
    elif f"{prefix}help" in message.content:
        embed = discord.Embed(title = "Hoi! Wonky Tonky?",description=f'''
        
**Harleen**
Prefix: h!
I am Harleen, people call me a bot, but professionally I'm a mastermind
My powers of multi tasking, well its immatchable

> *Whenever I try moving on one path,* 
> *Others are auto attracted towards me*

**Commands:**
{prefix}help- Display this command 
{prefix}hello - Hello!!
{prefix}meme - Get your stomach punky with a meme 
{prefix}reddit <subreddit> - Ah yes get posts from your favorite subreddit, right in discord
{prefix}surprise <user> - Give a good surprise to your best friend/enemy
{prefix}joke - Wanna listen to a panky joke?
{prefix}short <url> <alias type> <alias> - Get a shortened custom url free of cost
{prefix}quote - Wanna refresh your brain with some motivating quotes?
harley <question> - You can chat with me with basic questions, cmon don't be so tough
{prefix}getinv - Get an invite link for the current server.
{prefix}src - Wanna peek in inside me?

**Browsing Section:**
{prefix}google <argument> - Can't undertsand soemthing? Google it!
{prefix}wiki <argument> - Oh how much I like to read wikipedia articles
{prefix}yt <argument> - Search your fav video on Youtube can you?
{prefix}gif <argument> - Get your desired GIFs!
harley how to do <terms> - Confused on seomthing? Ask it her

**Reactions**:
{prefix}yes 
{prefix}no 
{prefix}yay 
{prefix}lol
{prefix}sus
{prefix}damnson

Have Fun ;)

Happy Biting!

''' ,color=discord.Color.red())
        embed.set_image(url="https://c.tenor.com/52Z-ocm88pcAAAAC/harley-quinn-eyebrows.gif")
        await message.channel.send(embed=embed)


# ---------------------------------------------------------------------------------------

    # Secret Command to Rickroll your friend
    elif f"{prefix}surprise" in message.content:
        cn = (message.content)[10:] # Fetch user ping
        await message.channel.guild.create_text_channel("party") # Make a seperate channel for rickroll
        i = 0
        channel = discord.utils.get(message.channel.guild.channels, name='party') # Identify channel id
        while i<5:
            await channel.send(cn) # Ping the target 5 times
            i+=1
        await channel.send("https://c.tenor.com/Z6gmDPeM6dgAAAAC/dance-moves.gif") # Rick Roll gif
        time.sleep(30) # Wait 30 secs
        channel_id = channel.id
        channel = client.get_channel(channel_id)
        await channel.delete() # Purge the created channel

# ---------------------------------------------------------------------------------------

    # Lol reaction command
    elif message.content == f"{prefix}lol":
        await message.channel.send(choice(lolm))
    
    # Lol reaction command
    elif message.content == f"{prefix}yay":
        await message.channel.send(choice(yaym))
    
    elif message.content == f"{prefix}no":
        await message.channel.send(choice(nom))

    # Lol reaction command
    elif message.content == f"{prefix}yes":
        await message.channel.send(choice(yesm))

    elif message.content == f"{prefix}sus":
        await message.channel.send(choice(susm))

    # Lol reaction command
    elif message.content == f"{prefix}damnson":
        await message.channel.send("DAMN SON! \n" + (choice(dms)))

# ---------------------------------------------------------------------------------------

    # Quoting command
    elif message.content == f'{prefix}quote':
        q, a = get_quote()
        em = cembed(title=a+" once said", description=q)
        await message.channel.send(embed=em)

# ---------------------------------------------------------------------------------------

    # Search YT command
    elif message.content.startswith(f"{prefix}yt"):
        message.content=message.content.strip(f'{prefix}yt')
        await message.channel.send(searchyt(message.content))
    
# ---------------------------------------------------------------------------------------

    # Google Search Command
    elif message.content.startswith(f"{prefix}google"):
        cont = (message.content).replace(f'{prefix}google', "")
        for j in googlesearch.search(cont, 5, 5, 0):
            await message.channel.send(j)
    elif message.content.startswith(f"{prefix}googol"):
        cont = (message.content).replace(f'{prefix}googol', "")
        for j in googlesearch.search(cont, 1, 1, 0):
            await message.channel.send(j)

# ---------------------------------------------------------------------------------------

    
    # Wikipedia Search
    elif message.content.startswith(f"{prefix}wiki"):
        cont = (message.content).replace(f'{prefix}wiki', "")
        cont = (message.content).replace('\n', "")
        
        try:
            results = wikipedia.summary(cont, sentences=2) 
            ny = wikipedia.page(cont)
            await message.channel.send(results)
            await message.channel.send(ny.url)
        except Exception:
            await message.channel.send('Page not found')
    
    # Joke generation
    elif message.content==f"{prefix}joke":
        jk=pyjokes.get_joke(language='en', category= 'neutral')
        await message.channel.send(jk)
    
    # Meme generation
    elif message.content==f"{prefix}meme":
        await message.channel.send(getmeme('memes'))
        
    # Random image from subreddit commamd
    elif f"{prefix}reddit" in message.content:
        cn = message.content[9:]
        await message.channel.send(getmeme(cn))
        
    # Basic Chatbot system 
    elif (message.content.lower()).startswith(f'harley'):
        cn = message.content[7:].lower()
        if 'what do you eat' in cn or 'eat something' in cn or 'can you eat' in cn:
            holl =["I can't eat as I'm a bot ofcourse", "Nothing for now, Your head in future", "Human Flesh, wanna have some?"]
            await message.channel.send(choice(holl))
        elif 'who is your creator' in cn or 'who made you' in cn or 'who created you' in cn:
            holl =["I was created by @JAY#5059", "I was given birth by a male homosapien @JAY#5059 ... HEAVY SUS", "I was literally made by a person who flexes to be a god"]
            await message.channel.send(choice(holl))
        elif 'what is your age' in cn or 'when were you born' in cn or 'how old are you' in cn:
            holl =["I was created on 24.08.2021 by Jay", "I was born on 24.08.2021", "It's just a matter of few months"]
            await message.channel.send(choice(holl))
        elif 'what are you doing currently' in cn or 'what are your future plans' in cn or 'what is jay doing' in cn:
            holl =["We are working on the next video which is secret! Dropping in soon tho.", "Jay is preparing for his exams and I'm helping him :)", "I'm pretty sure Jay is working on a new project soon"]
            await message.channel.send(choice(holl))
        elif 'why are you here' in cn or 'what can you do' in cn or 'what are your skills' in cn:
            holl =["I am here to take care of heavy stuff here. People use me for utility, fun and entertainment, and even for expressing their thoughts with my fun filled GIFs"]
            await message.channel.send(choice(holl))
        elif 'do you know jay' in cn or 'who is jay' in cn:
            holl = ["Ofcourse, Jay is the admin of this server and holds the Jay Tech Titan youtube channel https://www.youtube.com/channel/UCyyXcHm8UswsF0cjOX6fMng", "Jay is an awesome guy who loves helping others, he even has a youtube channel calls=ed Jay Tech Titan"]
            await message.channel.send(choice(holl))
        elif 'do firmware update' in cn or 'firmware update' in cn:
            await message.channel.send("I cannot update firmware cuz I don't like lazy people")
            await message.channel.send("Do it yourself.")
            for j in googlesearch.search("how to update firmware", 1, 1, 0):
                await message.channel.send(j)
        elif 'btwihavenoname' in cn or 'btwnoname' in cn:
            await message.channel.send("Linus said it was GPL, LINUS said it was gud code")
        elif "how to do" in cn:
            cont = (message.content).replace(f"harley", "")
            await message.channel.send("I found this that may help you:\n\n")
            for j in googlesearch.search(cont, 1, 1, 0):
                await message.channel.send(j)
        else:
            cont = (message.content).replace(f"harley", "")
            from prsaw import RandomStuff
            rs = RandomStuff(async_mode=True,api_key=CBAPI)
            res = await rs.get_ai_response(cont);await rs.close()
            await message.channel.send(res[0]["message"])
    
    elif message.content == f"{prefix}src":
        em = discord.Embed(title="Source Code", description="My source code is at:\n https://github.com/arghyagod-coder/Harleen", color=discord.Color.blue())
        em.set_image(url="https://media4.giphy.com/media/ujBfE6zDRAcYU/giphy.gif?cid=ecf05e47bvt5rlojly56yq9yksf6petiznpw7waboj0olscz&rid=giphy.gif&ct=g")
        await message.channel.send(embed = em)



    elif message.content == f"{prefix}hello":
        await message.channel.send(f"Hello {message.author.mention} !")
    
        # elif f"{prefix}prefix" in message.content:
        #     cont = message.content.replace(f'{prefix}prefix ', '')
        #     with open('guilds.json') as f:
        #         x = json.load(f)
        #         guild = discord.utils.get(client.guilds, name=GUILD)
        #         x[guild.id] = cont
        #         json.dump(x, f)
            # await message.channel.send(jk)
    
    elif message.content == f"{prefix}getinv":
        invite = await message.channel.create_invite()
        await message.channel.send(f"Here you go my boi: {invite} ")
    
    elif f"{prefix}gif" in message.content:
        import TenGiphPy
        cont = (message.content).replace(f'{prefix}gif', "")
        t = TenGiphPy.Tenor(token=TKEY)
        await message.channel.send(t.random(cont))
    
    elif f"{prefix}ping" in message.content:
        cont = (message.content).replace(f'{prefix}ping ', "")
        li = cont.split()
        n = int(li[-2])
        p = li[-1]
        i=0
        if n>20:
            message.channel.send("Shut your mischief man\nDon't be such a noob")
        else:
            while i<n:
                await message.channel.send(p)
                i+=1
			
    elif f"{prefix}waifu" in message.content:
        from waifu import WaifuClient
        wc= WaifuClient()
        sfw_waifu: str = wc.sfw(category='waifu')
        em = cembed(title="Oh Ho Boi", description="Cute?", picture=sfw_waifu)
        await message.channel.send(embed=em)
    
    elif f"{prefix}weather" in message.content:
        cn=message.content[9:]
        import randomstuff
        rs = randomstuff.AsyncClient(api_key=CBAPI)
        res = await rs.get_weather(cn.lower())
        em = discord.Embed(title=f"Weather at {res.location.name} is:", description=f"{res.current.temperature}??C", color=discord.Color.blue())
        rs.close()
        await message.channel.send(embed=em)
    elif f"{prefix}slap" in cm:
        cl = cm.split()
        ct = cl[1]
        em = discord.Embed(description=f"{message.author.name} gives a tight smack to {ct}!", color=discord.Color.blue())
        import TenGiphPy
        t = TenGiphPy.Tenor(token=TKEY)
        em.set_image(url=(t.random("batman slap")))
        await message.channel.send(embed = em)
    elif f"{prefix}kick" in cm:
        cl = cm.split()
        ct = cl[1]
        em = discord.Embed(description=f"{message.author.name} throws out {ct}, K.O.!", color=discord.Color.blue())
        import TenGiphPy
        t = TenGiphPy.Tenor(token=TKEY)
        em.set_image(url=(t.random("batman kick")))
        await message.channel.send(embed = em)
    elif f"{prefix}punch" in cm:
        cl = cm.split()
        ct = cl[1]
        em = discord.Embed(description=f"{ct} is done this time by... {message.author.name}!", color=discord.Color.blue())
        import TenGiphPy
        t = TenGiphPy.Tenor(token=TKEY)
        em.set_image(url=(t.random("batman punch")))
        await message.channel.send(embed = em)
    elif f"{prefix}kill" in cm:
        cl = cm.split()
        ct = cl[1]
        em = discord.Embed(description=f"{message.author.name} seems to have made someone disappear... \n Is it {ct}?", color=discord.Color.blue())
        import TenGiphPy
        t = TenGiphPy.Tenor(token=TKEY)
        em.set_image(url=(t.random("batman killing")))
        await message.channel.send(embed = em)
    elif f"{prefix}gayrate" in cm:
        cl = cm.split()
        pr= random.randint(1, 100)
        ct = cl[1]
        em = discord.Embed(description=f"{ct} is {pr}% gay\n:rainbow_flag: :thinking:", color=discord.Color.red())
        await message.channel.send(embed=em)

    elif f"{prefix}aw" in message.content:
        try:
            cont = (message.content).replace(f'{prefix}aw ', "")
            print(cont)
            page = requests.get(f'https://wiki.archlinux.org/title/{cont}')
            soup = bs4.BeautifulSoup(page.content, "html.parser")
            title = soup.find_all('title', limit=1)
            para = soup.find_all('dd', limit=1)
            embed=discord.Embed(title=title[0].string, url=f"https://wiki.archlinux.org/title/{cont}", description=para[0].get_text(), color=discord.Color.blue())
            embed.set_author(name="ArchLinux Wiki", url="https://wiki.archlinux.org/", icon_url="https://wiki.installgentoo.com/images/f/f9/Arch-linux-logo.png")
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Arch_Linux_logo.svg/800px-Arch_Linux_logo.svg.png")
            await message.channel.send(embed=embed)
        except Exception:
            page = requests.get(f'https://wiki.archlinux.org/index.php?search={cont}&title=Special%3ASearch&go=Go')
            soup = bs4.BeautifulSoup(page.content, "html.parser")
            titles = soup.find_all( class_ = "mw-search-result", limit=9)
            suggestions = []
            for title in titles:
                suggestions.append(title.get_text().split(' ')[0])

            embed=discord.Embed(title="404 Not Found", url=f"https://wiki.archlinux.org/title/{cont}", description=f"The keyword entered by you were not found\n\n**Suggestions:**\n\n{','.join(suggestions)}", color=discord.Color.red())
            embed.set_author(name="ArchLinux Wiki", url="https://wiki.archlinux.org/", icon_url="https://wiki.installgentoo.com/images/f/f9/Arch-linux-logo.png")
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Arch_Linux_logo.svg/800px-Arch_Linux_logo.svg.png")
            await message.channel.send(embed=embed)

    elif f"{prefix}warn" in message.content:
        cont = (message.content).replace(f'{prefix}warn ', "")
        tl = cont.split(',')
        em = discord.Embed(title="Warn Notice!", description=f"{tl[0]} was accused of {tl[1]}. If you agree with {message.author.name}, mention your decision through vote", color=discord.Color.red())
        msg = await message.channel.send(embed=em);up = "????";down = "????";
        await msg.add_reaction("????")
        await msg.add_reaction("????")
        valid_reactions = ["????", "????"]
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in valid_reactions
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        if reaction==up:
            await message.channel.send("Up pressed")
        elif reaction==down:
            await message.channel.send("Up pressed")

# Uptime Robot Regularization


# Run discord app
bot.run(str(TOKEN))
# client.run(TOKEN)
keep_alive()