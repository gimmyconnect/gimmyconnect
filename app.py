import telebot

bot = telebot.TeleBot("token")

@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.reply_to(message, "Siema")

bot.polling(none_stop=True)
