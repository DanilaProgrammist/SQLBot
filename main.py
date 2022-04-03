import telebot


from BDtest import build_bd

from Del_user import del_user
from Set_user import set_user
from Find_user import find_user


from Token import token
from telebot import types
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row("Добавить пользователя✋", "Найти пользователя🧐", "Удалить пользователя😵")

bot = telebot.TeleBot(token)
build_bd()

@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text'])
def start_message(message):
  command = bot.send_message(message.chat.id,"Привет ✌, Что бы ты хотел сделать?", reply_markup=keyboard )
  bot.register_next_step_handler(command, commands)

@bot.message_handler(func=lambda message: True)
def commands(message):
    if message.text == "Добавить пользователя✋":
        name = bot.send_message(message.chat.id, "введите имя", reply_markup= None)
        bot.register_next_step_handler(name, set_name)
    if message.text == "Найти пользователя🧐":
        name = bot.send_message(message.chat.id, "пришлите имя",reply_markup= None)
        bot.register_next_step_handler(name, find_name)
    if message.text == "Удалить пользователя😵":
        name = bot.send_message(message.chat.id, "введите имя", reply_markup= None)
        bot.register_next_step_handler(name, del_name)
    if message.text != "Добавить пользователя✋" and message.text != "Найти пользователя🧐" and message.text != "Удалить пользователя😵":
        bot.send_message(message.chat.id, "я не понимаю :(", reply_markup=None)
        new_answer = bot.send_message(message.chat.id, "Напиши ещё раз")
        bot.register_next_step_handler(new_answer, commands)
def set_name(message):
    bot.send_message(message.chat.id, "Пользователь добавлен")
    command = bot.send_message(message.chat.id, "Дальше?", reply_markup= keyboard)
    set_user(message.text)
    bot.register_next_step_handler(command, commands)
def find_name(message):
    bot.send_message(message.chat.id, str(find_user(message.text)))
    command = bot.send_message(message.chat.id, "Дальше?", reply_markup= keyboard)
    bot.register_next_step_handler(command, commands)
def del_name(message):
    bot.send_message(message.chat.id, str(del_user(message.text)))
    command = bot.send_message(message.chat.id, "Дальше?", reply_markup= keyboard)
    del_user(message)
    bot.register_next_step_handler(command, commands)

bot.polling()