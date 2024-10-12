import telebot

token = "7405174185:AAHs_zchuRB744jUREoo86FQgws_mlfk93Q"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.infinity_polling()