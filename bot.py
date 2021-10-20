#import discord library and bot serv
import os
import discord
from botServ import botServ

#discord client to send commands
bot = discord.Client()

#on start
@bot.event
async def on_ready():
  print("Bot connected")

#post jpg file when key word is typed
@bot.event
async def on_message(message):
  if 'tren' in message.content or 'Tren' in message.content:
    await message.channel.send("Did someboady say... TREN!?!?")
    await message.channel.send(file=discord.File('tren.jpg'))

botServ()
TOKEN=("Enter discord token here")
bot.run(TOKEN)
