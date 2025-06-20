import os
import telebot
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "नमस्ते! 🙏 मैं DhiGuruBot हूँ — आपके सवालों का जवाब देने को तैयार हूँ।")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"आपने कहा: {message.text}")

print("Bot is running...")
bot.infinity_polling()
