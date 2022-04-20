import random
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
import uuid
import calendar
import time
ts = calendar.timegm(time.gmtime())

# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(ts)]
last_5_digit = (res[6:])

account_number = (res[3:])

def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))
    return (res)


def otp_Verification():

    list = last_5_digit
    token_convert=(convert(list))
    radnum= (random.randint(token_convert, 774241))

    return radnum   # print(ts)

def account_number_generator():

    list = account_number[4:7]
    account_number_convert = (convert(list))
    print('this is', account_number_convert)
    radnum = (random.randint(account_number_convert, 7742415))
    user_account_number = '433' + str(radnum)
    return user_account_number


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.last_login)
        )

account_activation_token = TokenGenerator()
