import telebot
import os

TOKEN = os.getenv("8305742502:AAHsdQ69n-JWxvShkpn6YFLm431PmuZ2OXc")
bot = telebot.TeleBot(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)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! I'm your trading helper bot 🔥")

@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    bot.reply_to(message, "📸 Got your screenshot! I'll analyze it soon.")

bot.polling()
