import os
import telebot
from telebot import types
from flask import Flask

bot = telebot.TeleBot("7667965160:AAFVbRt8GeYhusJZx93u1953VfOabIRXR3o")
app = Flask(__name__)

@app.route('/')
def index():
    return "Бот працює!"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Абоба")

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "/start - запуск бота \n/help - усі команди")

def start_bot():
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"Помилка: {e}")

if __name__ == '__main__':
    from threading import Thread
    Thread(target=start_bot).start()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
