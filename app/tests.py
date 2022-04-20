from django.test import TestCase

# Create your tests here.
import telegram


#token that can be generated talking with @BotFather on telegram
my_token = '1952165487:AAHtwNQPRDk2IuB-75e75wTbkaVgcaJwNbA'

def send(msg, chat_id, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)


send('Hy', '1553402004')