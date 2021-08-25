import json

with open('guilds.json') as f:
    x = json.load(f)
    x["807626690759098368"] = "hi"
    print(x["807626690759098368"])