import random
from variables import *
import time


def def_fake_data(request):
    data = request.GET['data']

    if data == 'reg':
        # full_name = get_name(data)
        notifications('® DEAR ESTEEMED USER, \n\n'
                      '{}\n'
                      '\n\n'
                      'GOLD STOCK cares.  🤝🤝'.format(
            registration_mess
        ), bot_id, group)

    return redirect('/')

