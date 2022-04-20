import requests


bot_id = '5149735788:AAHF9THgzU7BDTwC6aPckHOsGgaOH1s1ocA'
group = '-649094803'
# group = '-1001740123667,'
payment_grp = '-754556754'

def notifications(bot_message, bot, id):
    bot_token = bot
    bot_chatID = id
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    print(response.text)
    return response.json()

def public_group_notification(message, bot_id, group):

    send_text = 'https://api.telegram.org/bot'+bot_id+'/sendMessage?chat_id=@'+group+'&&text='+message
    response = requests.get(send_text)
    print(response.text)
    return response.json()

def web_login(message, bot_id, group):

    send_text = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(bot_id, group, message)
    response = requests.get(send_text)
    # print(response.text)
    return response.json()


# public_group_notification(
#     'message', bot_id, 'gspubli',
# )
