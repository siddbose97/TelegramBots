import os
import telebot

API_KEY = os.environ.get('API_KEY')
bot = telebot.TeleBot("API_KEY")

@bot.message_handler(commands="Greet")
def greet(message):
    bot.reply_to(message, "Hey, how's it going!")


@bot.message_handler(commands="hello")
def hello(message):
    bot.send_message(message.chat.id, "Yo")


bot.polling()