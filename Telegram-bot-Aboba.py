import telebot
from telebot import types
name =''
bot = telebot.TeleBot("6880422905:AAFSSfSh38NxEyluwZglfCKivX9b2zp_6g8")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Салаам Алейкум, і я продовжу терор на новому рівні. МУХАХАХАХА")

@bot.message_handler(func=lambda message: message.text.lower() in ["ги", "Ги"])
def greet_user(message):
    bot.send_message(message.chat.id, "Привіт! Як справи? 😊")


bot.infinity_polling()