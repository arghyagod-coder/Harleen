# Imports

import os # For fetching ENV SECRETS
from keep_alive import keep_alive # Uptime Robot SRC file
import random # Choice
from random import choice
from youtube_search import * # pip install youtube_search
import time # Sleep functions
import discord # pip install discord.py
import praw # pip install praw
import pyjokes # pip install pyjokes
from googlesearch import search # pip install beautifulsoup4 google
import requests, json, wikipedia # pip install requests wikipedia
from dotenv import load_dotenv # pip install python-dotenv
from titan import shorten # Shortning urls with titan

# Fetching environment variables (API keys and private stuff)
load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN') 
GUILD = os.getenv('DISCORD_GUILD')
REDDIT_CID = os.getenv('REDDIT_CID')
REDDIT_SCT = os.getenv('REDDIT_SCT')

# Initializing Discord Client
client = discord.Client()

# Function to get memes from praw (Python Reddit API Wrapper)
def getmeme(topic): # Topic/Subreddit name
    reddit = praw.Reddit(client_id=REDDIT_CID,
                    client_secret=REDDIT_SCT,
                    user_agent='meme') # Initializing details

    submission = reddit.subreddit(topic).random()
    return submission.url

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

# GIFs for No Reaction
nom = [
    "https://giphy.com/gifs/the-office-mrw-d10dMmzqCYqQ0",
    "https://giphy.com/gifs/NetflixisaJoke-netflix-iglesias-mr-h5cl6eHMvf0IQ3wJch",
    "https://giphy.com/gifs/memecandy-J46T6SB3yzwc4eBYeL"
]

# Use of Zenquotes API to fetch motivating quotes
def get_quote():
    res = requests.get("https://zenquotes.io/api/random")
    jsond= json.loads(res.text)
    quote = jsond[0]['q'] + '\n\n -' + ("> "+(jsond[0]['a']))
    return quote

# Use of youtubesearch module to fetch youtube results
def searchyt(cont):
    results = YoutubeSearch(str(cont), max_results=1).to_dict()
    sp = results[0]["id"]
    url = "https://youtu.be/" + sp
    return url

# Starting success message after Initialization
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# Function to DM people who join the server (unfunctional for now)
@client.event
async def on_member_join(member):
    guild = discord.utils.get(client.guilds, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to {guild.name}!'
    )

# Function executing on a message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Func- Shorten URLs with titanURL 
    if message.content.startswith("%short"):
        queries = (message.content).replace(
            "%short", "").lstrip().rstrip().split(" ")
        if len(queries) == 1:
            await message.channel.send(shorten(queries[0]))
        elif len(queries) == 2:
            await message.channel.send(shorten(queries[0], queries[1]))
        elif len(queries) == 3:
            await message.channel.send(shorten(queries[0], queries[1], queries[2]))
        else:
            await message.channel.send("Invalid query! The command syntax is `binod.shorten <url_to_shorten> <alias_type> <alias>`.")
    elif "%help" in message.content:
        await message.channel.send('''
        
**Harleen**
I am Harleen, people call me a bot, but professionally I'm a mastermind
My powers of multi tasking, well its immatchable

> *Whenever I try moving on one path,* 
> *Others are auto attracted towards me*

**Commands:**
%help- Display this command 
%meme - Get your stomach punky with a meme 
%reddit <subreddit> - Ah yes get posts from your favorite subreddit, right in discord
%surprise <user> - Give a good surprise to your best friend/enemy
%joke - Wanna listen to a panky joke?
%short <url> <alias type> <alias> - Get a shortened custom url free of cost
%quote - Wanna refresh your brain with some motivating quotes?
%chat <question> - You can chat with me with basic questions, cmon don't be so tough

**Browsing Section:**
%google <argument> - Can't undertsand soemthing? Google it!
%wiki <argument> - Oh how much I like to read wikipedia articles
%yt <argument> - Search your fav video on Youtube can you?

**Reactions**:
%yes 
%no 
%yay 
%lol
%damnson

Have Fun ;)

Happy Biting!

https://c.tenor.com/52Z-ocm88pcAAAAC/harley-quinn-eyebrows.gif
''')
    # Secret Command to Rickroll your friend
    elif "%surprise" in message.content:
        cn = (message.content)[9:] # Fetch user ping
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

    # Lol reaction command
    elif message.content == "%lol":
        await message.channel.send(choice(lolm))
    
    # Lol reaction command
    elif message.content == "%yay":
        await message.channel.send(choice(yaym))
    
    elif message.content == "%no":
        await message.channel.send(choice(nom))

    # Lol reaction command
    elif message.content == "%yes":
        await message.channel.send(choice(yesm))

    # Lol reaction command
    elif message.content == "%damnson":
        await message.channel.send("DAMN SON! \n" + (choice(dms)))

    # Quoting command
    elif message.content == '%quote':
        await message.channel.send('> '+get_quote())

    # Search YT command
    elif message.content.startswith("%yt"):
        await message.channel.send(searchyt(message.content))
    
    # Google Search Command
    elif message.content.startswith("%google"):
        cont = (message.content).replace('%google', "")
        for j in search(cont, 5, 5, 0):
            await message.channel.send(j)
    
    elif "%exe" in message.content:
        import subprocess as sb
        out = sb.check_output(f'echo "{message.content[5:]}">>file.py; python3 file.py; rm file.py', shell=True)
        out = out.decode('utf-8')
        await message.channel.send(out)
    # Wikipedia Search
    elif message.content.startswith("%wiki"):
        cont = (message.content).replace('%wiki', "")
        cont = (message.content).replace('\n', "")
        
        try:
            results = wikipedia.summary(cont, sentences=2) 
            ny = wikipedia.page(cont)
            await message.channel.send(results)
            await message.channel.send(ny.url)
        except Exception:
            await message.channel.send('Page not found')
    
    # Joke generation
    elif message.content=="%joke":
        jk=pyjokes.get_joke(language='en', category= 'neutral')
        await message.channel.send(jk)
    
    # Meme generation
    elif message.content=="%meme":
        await message.channel.send(getmeme('memes'))
        
    # Random image from subreddit commamd
    elif "%reddit" in message.content:
        cn = message.content[8:]
        await message.channel.send(getmeme(cn))
        
    # Basic Chatbot system 
    elif message.content.startswith('%chat'):
        cn = message.content[6:].lower()
        if 'hi' in cn or 'hello' in cn or 'wassup' in cn or 'whats up' in cn or 'is anyone there' in cn or 'good day' in cn or 'how are you' in cn or 'hey' in cn or 'greetings' in cn or 'bonjour' in cn or 'hola' in cn or "i'm back" in cn:
            holl = ["Hello!", "Good to see you again!", "Hi there, how can I help?"]
            await message.channel.send(choice(holl))
        elif 'cya' in cn or 'goodbye' in cn or 'good bye' in cn or 'gtg' in cn or 'see you later' in cn or 'i am leaving' in cn or 'have a good day' in cn or 'bye' in cn or 'ciao' in cn or 'bye bye' in cn or 'have to go' in cn or "bye..." in cn:
            holl =["Sad to see you go :(", "Talk to you later", "Goodbye!"]
            await message.channel.send(choice(holl))
        elif 'what do you eat' in cn or 'eat something' in cn or 'can you eat' in cn:
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

# Uptime Robot Regularization
keep_alive()

# Run discord app
client.run(TOKEN)
my_secret = os.environ['DISCORD_TOKEN']