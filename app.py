import telebot

bot = telebot.TeleBot("8497228841:AAGVTU5PUHaqVcq69c9eqnvpZ1vmfBLNPQk")

@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.reply_to(message, "Siema")

bot.polling(none_stop=True)
