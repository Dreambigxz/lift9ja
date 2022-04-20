import requests
import json
import ast
from percent_calculator import percentage_calculator
import re
#
# curl --location --request POST 'https://honourworld.ng/datatopup?callback=jQuery341029082756535757914_1640621070197' \
# --header 'Cookie: yourCookie' \
# --header 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' \
# --form 'action="get-plan"' \
# --form 'id="12"'

def get_all_categories_plan(plan_id, resell_percent, cg_data_active):
    url = "https://honourworld.ng/datatopup?callback=jQuery341029082756535757914_1640621070197"

    data = 'action=get-plans&id={}'.format(plan_id)
    headers = {
        'Cookie': 'PHPSESSID=; lang=en-US; nplh=5497.8605c047867f6f05e82c25e20f734ff1; nplrmm=1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.request("POST", url, headers=headers, data=data)
    data = r.text.replace("\\", '').replace('jQuery341029082756535757914_1640621070197', '').replace('u20a6', '').replace('(', '',).replace(')', '')
    data = data.replace('"[', '(').replace(']"', ')')
    data = ast.literal_eval(data)

    # print(data)

    data = data['data']
    count = 0
    get_all_data = []

    for i in data:
        get_text = i['text'].replace('-', '')
        text = get_text.split()

        bought_price = (text[-1].replace(',', ''))
        remove_bought_price = get_text.replace(text[-1], '')

        get_data_value = (text[0].replace('GB', ' ').replace('MB', ' '))
        # print(get_data_value)

        # print(remove_bought_price)
        bought_price = float(bought_price)
        sale_price = percentage_calculator(resell_percent, bought_price)

        rmp = percentage_calculator(0, bought_price)

        if cg_data_active == True:
            add_new_price = '{} ₦{:,}'.format(remove_bought_price, sum([sale_price, bought_price]) - rmp)
        else:
            add_new_price = '{} ₦{:,}'.format(remove_bought_price, sum([sale_price, bought_price]))

        # i['amount'] = bought_price''
        cvt_float = ((float((get_data_value))))
        get_data_value = int(cvt_float)

        bought_price = bought_price - rmp
        get_all_data.append(({
            'id': i['id'],
            'text': add_new_price,
            'amount': bought_price,
            'data_value': get_data_value
        }))
        count += 1

        if len(data) == count:
            # print(get_all_data)
            return get_all_data

        # print(get_all_data)

def buy_data(category, plan_id, number):
    url = 'https://honourworld.ng/datatopup'
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'PHPSESSID=; lang=en-US; nplh=5497.8605c047867f6f05e82c25e20f734ff1; nplrmm=1',
        'referer': 'https://honourworld.ng/products/data-top-up',
        'user - agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 97.0.4692.71Safari / 537.36'

    }

    data = {
        'action': "data-topup",
        'category_id': category,
        'plan_id': plan_id,
        'contact_opt': "2",
        'phone_num': number

    }

    r = requests.post(url, headers=headers, data=data)
    data = (r.content)
    data_decode = data.decode('utf8')
    cvt_to_dict = json.loads(data_decode)
    # print('this is ', cvt_to_dicta
    return cvt_to_dict

# get_all_categories_plan(12, 0, cg_data_active=True)

