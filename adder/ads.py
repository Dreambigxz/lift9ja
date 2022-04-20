import requests



def telegram_bot_sendtext(bot_message):
    bot_token = '1904721083:AAEXt2lhnEPRsJwk2GjTbkmpDNAPADF14v4'
    bot_chatID = '402753789'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


# test = telegram_bot_sendtext("Testing Telegram bot")
