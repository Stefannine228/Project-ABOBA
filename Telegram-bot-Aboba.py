import telebot
import random
import time
import asyncio

bot = telebot.TeleBot("7667965160:AAFVbRt8GeYhusJZx93u1953VfOabIRXR3o")
admins=['Dyda275','TypaKlutoy']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Абоба")

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "/start - запуск бота \n/help - усі команди\n/aboba")

@bot.message_handler(content_types=['text'])
def check_messages(message):
    if message.text.lower() == 'абоба':
        bot.send_message(message.chat.id, random.choice(['абоба', 'Абоба', 'АБОООБААА','абоба', 'Абоба', 'АБОООБААА','абіба']))
    elif message.text.lower() in ["ні", "ні.","нє","нє","ні!","нє!","нэ","нэ!","нэ.","нє."]:
        bot.send_message(message.chat.id, "Ні? Пішов тоді ти нахуй! Рицаря затримав!")

@bot.message_handler(commands=['aboba'])
def start_message(message):
    bot.send_message(
        message.chat.id, 
        '<a href="https://youtu.be/dQw4w9WgXcQ?si=Dwe0iKSP48FbgAdF">aboba тут</a>', 
        parse_mode="HTML",
        disable_web_page_preview=True  # Вимикає прев’ю посилання
    )

@bot.message_handler(commands=['info'])
def main(message):
 bot.send_message(message.chat.id, message)
 

GROUP_ID = '2105518856'  # Ваш канал або група
@bot.message_handler(commands=['test'])
def send_to_group(text):
    bot.send_message(GROUP_ID, text)

@bot.message_handler(commands=['admin'])
def main(m):
 if m.from_user.username in admins:
  bot.send_message(m.chat.id, m.from_user.username + " administrator aboba")



bot.polling()

  
bot.polling(none_stop=True, timeout=60)