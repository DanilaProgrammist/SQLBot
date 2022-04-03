from Token import token
import telebot
import sqlite3
from Token import token
from telebot import types
keyboard = types.ReplyKeyboardMarkup()
keyboard.row("Ввести данные", "Посмотреть данные", "Удалить данные")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌, Что бы ты хотел сделать?", reply_markup=keyboard )
@bot.message_handler(content_types=['text'])
def next_message(message):
  bot.send_message(message.chat.id, "Ты еблан?", reply_markup=keyboard)

bot.polling()

