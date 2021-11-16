import telebot

bot_token = "2032034697:AAFLQH09fuTXAFCjr7uVa6SUXFAqGhyUc08"
bot = telebot.TeleBot(bot_token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ويييه يا شب ")


if __name__ == '__main__':
    bot.infinity_polling()
