import os
import telebot
from openai import OpenAI

# Get keys from environment (safe method)
BOT_TOKEN = os.getenv("8305742502:AAHsdQ69n-JWxvShkpn6YFLm431PmuZ2OXc")
OPENAI_API_KEY = os.getenv("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")

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hello! I'm your trading assistant bot. Send me your message or trading screenshot for analysis.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a trading expert. Analyse the user's message and give useful advice."},
                {"role": "user", "content": message.text}
            ]
        )
        reply = response.choices[0].message.content
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")

print("✅ Bot is running...")
bot.infinity_polling()
