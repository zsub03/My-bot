import telebot

TOKEN = "8759340101:AAHQKCwBVKzDtyKeidxytgV8tm7uGXrIzP0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    bot.reply_to(message, "ចង់ខ្ចីលុយមែន?")

bot.polling()
