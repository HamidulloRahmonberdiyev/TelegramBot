# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 21:10:27 2023

@author: hamid
"""

from transliterate import to_cyrillic, to_latin

import telebot

TOKEN = "6173893689:AAFhcskxFW0q-y2VcGZ7lUr7g0EeZnYHzxg"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
	answer = "Assalomu alaykum, Xush kelibsiz!"
	answer += "\nMatn kiritng:"
	bot.reply_to(message, answer)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Sizga qanday yordam berolaman? Savol yoki murojatingizni bot asoschisiga yo'llang! @Hamidullo_Rahmonberdiyev")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text
	if msg.isascii():
		answer = to_cyrillic(msg)
	else:
		answer = to_latin(msg)
	bot.reply_to(message, answer) 


bot.infinity_polling()