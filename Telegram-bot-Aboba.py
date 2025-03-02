import telebot
from telebot import types
name =''
bot = telebot.TeleBot("7667965160:AAFVbRt8GeYhusJZx93u1953VfOabIRXR3o")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Абоба")
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "/start - запуск бота \n /help - усі команди")
                     
bot.infinity_polling()
