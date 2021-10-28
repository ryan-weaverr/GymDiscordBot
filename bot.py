#import discord library and bot serv
import discord
from botServ import botServ
import re

#discord client to send commands
bot = discord.Client()

#on start
@bot.event
async def on_ready():
  print("Bot connected")
  
#event: post jpg file when keyword is typed
@bot.event
async def on_message(message):
  # converting message to lowercase to make checking easier 
  currentMessage = message.content.lower()

  # substituting symbols with spaces 
  substituedMessage = re.sub(r'[^\w]', ' ', currentMessage)
  
  # splitting on spaces and adding to HashSet for constant time complexity on search
  messageSet = set()
  messageSet = substituedMessage.split()

  #keyword checks
  if "tren" in messageSet:
    if message.author != bot.user:
      await message.channel.send("Did somebody say... TREN!?!?")
      await message.channel.send(file=discord.File('tren.jpg'))

botServ()
TOKEN=("Enter discord token here")
bot.run(TOKEN)
