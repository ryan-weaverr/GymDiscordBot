#import discord library and bot serv
import os
import discord
from botServ import botServ

#discord client to send commands
client = discord.Client()

#on start
@client.event
async def on_ready():
  print("Bot connected")


botServ()
TOKEN=("Enter discord token here")
client.run(TOKEN)
