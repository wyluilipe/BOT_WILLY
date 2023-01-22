import telebot
from telebot import types
from time import sleep

import random
import training
import Token


WELCOME_TEXT = 'Привет! Меня зовут Willy. Может познакомимся поближе?'
HELP_TEXT = 'Если я вдруг тебе надоем, просто напиши команду "/stop" и я отвалюсь.'


token = Token.token
bot = telebot.TeleBor(token)

bot.remove_webhook()


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, WELCOME_TEXT)


@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, HELP_TEXT)


@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		


while True:
	try:
		bot.polling(none_stop=True)
	except Exception as _ex:
		print(_ex)
		sleep(15)

