#run bot in separate thread
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Bot online"

def run():
  app.run(host='0.0.0.0',port=8080)

def botServ():
  t = Thread(target=run)
  t.start()