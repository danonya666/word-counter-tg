import os
import time
import socket
sock = socket.socket()
sock.bind(('', 5000))
sock.listen(1)
import telebot
from telebot import apihelper

IS_HEROKU = True
if not IS_HEROKU:
    apihelper.proxy = {'https':'https://167.71.182.175:3128'}

TOKEN = os.environ['TOKEN']

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    print(message)


while True:
    try:
        bot.polling()
    except:
        time.sleep(3)
