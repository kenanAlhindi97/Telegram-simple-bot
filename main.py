# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from telegram.ext import Updater
from telegram.ext import Dispatcher
from telegram.ext import CommandHandler
import logging
import telebot


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="عيب يا شب أنا البوت شيخ الشباب")


bot_token = "2032034697:AAFLQH09fuTXAFCjr7uVa6SUXFAqGhyUc08"
bot = telebot.TeleBot(bot_token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ويييه يا شب ")


if __name__ == '__main__':
    bot.infinity_polling()
