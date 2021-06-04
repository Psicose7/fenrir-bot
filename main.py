import discord
import os

'''
# If you are coding the bot on a local machine, use the python-dotenv pakcage to get variables stored in .env file of your project
from dotenv import load_dotenv
load_dotenv()
'''


no_result_message = '''Sorry, I can't find information on that Astromon. Make sure you spelled it correctly.'''
elements = ["fire", "water", "wood", "dark", "light"]
astromons = [""]

# instantiate discord client 
client = discord.Client()

# discord event to check when the bot is online 
@client.event
async def on_ready():
  print(f'{client.user} is ready!')

@client.event
async def on_message(message): 
    # make sure bot doesn't respond to it's own messages to avoid infinite loop
    if message.author == client.user:
        return  
    # lower case message
    message_content = message.content.lower()
    argsCount = len(message_content.split())
    message_split = message_content.split()
    if message_split[0] in elements:
        element = message_split[0]
        message_split.remove(element)
        astromon = ' '.join([str(i) for i in message_split])
        print(astromon)
    if message_split[0] == "super":
        await message.channel.send('super')
        if message_split[1] in elements:
            await message.channel.send(message_split[1])

client.run("NzU0NTA5MzYxMzQyMTg1NDcy.X11xmQ.RLziwAMLKcAEdeFbvBSnQreJIHQ")