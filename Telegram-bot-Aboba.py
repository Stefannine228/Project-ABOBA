import telebot
from telebot import types
import time

bot = telebot.TeleBot("7667965160:AAFVbRt8GeYhusJZx93u1953VfOabIRXR3o")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Абоба")

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "/start - запуск бота \n/help - усі команди")

while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        time.sleep(5)  # Пауза перед перезапуском
