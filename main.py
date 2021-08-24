import os
from keep_alive import keep_alive
import random
# from neuralintents import GenericAssistant
from random import choice
from youtube_search import *
import discord
from googlesearch import search
import requests, json, wikipedia
from dotenv import load_dotenv
from titan import shorten

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

# chatbot = GenericAssitant("intents.json")
# chatbot.train_model()
# chatbot.save_model()


dms = ["https://giphy.com/gifs/batman-film-qVID3J8fLrlZK", "https://giphy.com/gifs/homer-simpson-barney-batman-and-robin-pSFEEQMaNcFAQ", "https://giphy.com/gifs/hug-5sos-5-seconds-of-summer-BcOvvS5t0sxnG", 'https://giphy.com/gifs/joker-the-joaquin-phoenix-A7ZbCuv0fJ0POGucwV']

lolm = ['https://giphy.com/gifs/originals-lol-3o6ozvv0zsJskzOCbu', 'https://giphy.com/gifs/theoffice-episode-6-the-office-tv-bC9czlgCMtw4cj8RgH','https://giphy.com/gifs/moodman-lol-spit-take-Q7ozWVYCR0nyW2rvPW', 'https://giphy.com/gifs/moodman-funny-lol-laughing-fUYhyT9IjftxrxJXcE', 'https://giphy.com/gifs/laughing-despicable-me-minions-ZqlvCTNHpqrio', 
'https://giphy.com/gifs/laughing-applause-mike-tyson-wWue0rCDOphOE']
yaym = [
    "https://giphy.com/gifs/F9hQLAVhWnL56",
    "https://giphy.com/gifs/thegifys-gifys-5xaOcLGvzHxDKjufnLW",
    "https://giphy.com/gifs/studiosoriginals-dog-josh-freydkis-bad-woof-l41Ym8O8dbIG0XvFK",
    "https://giphy.com/gifs/sherlockgnomes-sherlock-l4pTfx2qLszoacZRS",
    'https://giphy.com/gifs/foxinternational-reaction-simpsons-celebrate-26tPplGWjN0xLybiU',
    "https://giphy.com/gifs/excited-screaming-jonah-hill-5GoVLqeAOo6PK",
    "https://giphy.com/gifs/excited-yes-30-rock-I24hjk3H0R8Oc"
]
yesm = [
    "https://giphy.com/gifs/theoffice-MNmyTin5qt5LSXirxd",
    "https://giphy.com/gifs/DffShiJ47fPqM",
    "https://giphy.com/gifs/dYZuqJLDVsWMLWyIxJ"
]
nom = [
    "https://giphy.com/gifs/the-office-mrw-d10dMmzqCYqQ0",
    "https://giphy.com/gifs/NetflixisaJoke-netflix-iglesias-mr-h5cl6eHMvf0IQ3wJch",
    "https://giphy.com/gifs/memecandy-J46T6SB3yzwc4eBYeL"
]

def get_quote():
    res = requests.get("https://zenquotes.io/api/random")
    jsond= json.loads(res.text)
    quote = jsond[0]['q'] + '\n\n -' + ("> "+(jsond[0]['a']))
    return quote
def searchyt(cont):
    results = YoutubeSearch(str(cont), max_results=1).to_dict()
    sp = results[0]["id"]
    url = "https://youtu.be/" + sp
    return url
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    guild = discord.utils.get(client.guilds, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to {guild.name}!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

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

    elif message.content == '%99':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    elif message.content == "%lol":
        await message.channel.send(choice(lolm))
    
    elif message.content == "%yay":
        await message.channel.send(choice(yaym))
    
    elif message.content == "%no":
        await message.channel.send(choice(nom))

    elif message.content == "%yes":
        await message.channel.send(choice(yesm))

    elif message.content == "%damnson":
        await message.channel.send("DAMN SON! \n" + (choice(dms)))

    elif message.content == '%quote':
        # response = random.choice(brooklyn_99_quotes)
        await message.channel.send('> '+get_quote())

    elif message.content.startswith("%yt"):
        await message.channel.send(searchyt(message.content))
    

    elif message.content.startswith("%google"):
        cont = (message.content).replace('%google', "")
        for j in search(cont, 5, 5, 0):
            await message.channel.send(j)
    
    elif message.content.startswith("%wiki"):
        cont = (message.content).replace('%wiki', "")
        cont = (message.content).replace('\n', "")
        results = wikipedia.summary(cont, sentences=2) 
        ny = wikipedia.page(cont)
        await message.channel.send(results)
        try:
            await message.channel.send(ny.url)
        except Exception:
            await message.channel.send('Page not found')
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
        

keep_alive()
client.run(TOKEN)
my_secret = os.environ['DISCORD_TOKEN']
