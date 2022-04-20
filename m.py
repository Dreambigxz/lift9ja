from variables import *
# import time

from django.conf import settings


registration_mess = 'Your registrations in GS is Successful, kindly login to your account and purchase SG gold of your choice'
bot_id = '5149735788:AAHF9THgzU7BDTwC6aPckHOsGgaOH1s1ocA'
group = '-1001740123667,'
test = '-649094803'

img = {
    'photo': open('closed.png', 'rb')
}

def m_notification(name, amount):
    mess = 'Your daily GS value  of ₦{:,} has been paid directly into your wallet balance.' \
           ' Kindly login to your dashboard and process withdrawals'.format(Decimal(amount))
    notifications('Withdrawal Due\n\n'
                  'Congratulations {}\n\n'
                  '{}\n\n'
                  '{} just getting started❤️'
                  .format(name.title(), mess, site_name),
                  bot_id, group)

def last_mess():
    mess = 'Your last GS value  of ₦{:,} has been paid directly into your wallet balance.' \
           ' Kindly login to your dashboard and process withdrawals'.format(Decimal('50'))
    notifications('Cheers 🍷🍷 {}\n\n'
                  '{}\n\n'
                  'Thanks for trusting us 🤝🤝,\n\n'
                  'We look forward to see you again as we promise not to fail any of our investors. 👊🏼\n'
                  '{} cares ❤️'
                  .format('Testing'.title(), mess, site_name),
                  bot_id, test)

def statistics():
    bill = admin.bill_settlement

    users = MyUser.objects.all().count()
    active_gs_count = UserGold.objects.filter(state='approved').exclude(user__is_admin=True).count()
    all_gs_count = UserGold.objects.filter().count()

    active_gs_bought = sum(
        [i.plan.amount for i in UserGold.objects.filter(state='approved').exclude(user__is_admin=True)])
    all_gs = sum([i.plan.amount for i in UserGold.objects.filter()])

    total_withdrawal_amount = sum([i.amount for i in
                                   WalletHistory.objects.filter(type='withdraw', status='success').exclude(
                                       user__is_admin=True)])

    balance = active_gs_bought - total_withdrawal_amount - bill

    total_gs = UserGold.objects.filter(state='approved',)
    active_gs =  UserGold.objects.filter(status='active', state='approved')
    get_today_active_gs = UserGold.objects.filter(status='active', state='approved', next_run_date=date.today())
    ending_today = UserGold.objects.filter(status='active', state='approved',end_date=date.today())

    get_today_active_gs = UserGold.objects.filter(status='active', state='approved', next_run_date=date.today())
    ended_gs = UserGold.objects.filter(status='ended')

    today_to_pay = sum([i.plan.daily_earn for i in get_today_active_gs])
    balance_after_paying = balance - today_to_pay

    notifications('Live GS STATISTICS  !!!\n\n'
                  'Total GS: {} \n'
                  'Active GS: {} \n'
                  'Ended GS: {} \n'
                  'Today\'s GS: {} \n'
                  'Total Ending Gs Today: {}\n'
                  'Total Bal to Pay ₦{:,}\n'
                  'Total Bal After Paying ₦{:,}'
                  .format(total_gs.count(),
                          sum([active_gs.count(), 0]), ended_gs.count(),
                          get_today_active_gs.count(), ending_today.count(),
                          sum([today_to_pay]), balance_after_paying),
                  bot_id, private_grp)

    print('Done')

def test_filtering():

    amounts = []
    get_today_active_gs = UserGold.objects.filter(status='active', state='approved', next_run_date=date.today()).order_by(
        'end_date'
    )

    for i in get_today_active_gs:
        amount = 'N{:,}'.format((i.plan.daily_earn))
        amounts.append(amount)

    print(amounts, get_today_active_gs.count())

def pay(num, start, stop):

    get_today_active_gs = UserGold.objects.filter(status='active', state='approved', next_run_date=date.today()).order_by(
        'end_date'
    )
    print(get_today_active_gs.count())
    get_today_active_gs = get_today_active_gs[:num]

    if get_today_active_gs.count() == 0:
        print('NO DATA')
        statistics()
    count = 0

    for i in get_today_active_gs:
        count += 1
        user_wallet = UserWallet.objects.get(user=i.user)
        # check if is end date
        if i.plan.daily_earn in range(start, stop):
            if i.end_date == date.today():
                i.total_earned += Decimal(i.total_left)
                user_wallet.user_balance += Decimal(i.total_left)
                user_wallet.testified = False

                mess = 'Your last GS value  of ₦{:,} has been paid directly into your wallet balance.' \
                       ' Kindly login to your dashboard and process withdrawals.\n\n' \
                       'You can also buy/sell data directly from your GS balance'.format(Decimal(i.total_left))
                notifications('Cheers 🍷🍷 {}\n\n'
                              '{}\n\n'
                              'Thanks for trusting us 🤝🤝,\n\n'
                              'We look forward to see you again as we promise not to fail any of our investors. 👊🏼\n'
                              '{} cares ❤❤️'
                              .format(i.user.full_name.title(), mess, site_name),
                              bot_id, group)

                i.total_left = 0
                i.status = 'ended'
                i.save()
                user_wallet.save()

            else:
                i.total_left -= Decimal(i.plan.daily_earn)
                i.total_earned += Decimal(i.plan.daily_earn)
                user_wallet.user_balance += Decimal(i.plan.daily_earn)
                user_wallet.testified = False

                if i.earn_after == '48':
                    i.next_run_date = current_timezone + timedelta(days=2)
                elif i.earn_after == '4days':
                    i.next_run_date = current_timezone + timedelta(days=4)
                else:
                    i.next_run_date = current_timezone + timedelta(days=1)

                i.save()
                user_wallet.save()

                mess = '🍷 Your daily GS value  of ₦{:,} has been paid directly into your wallet balance.' \
                       'Kindly login to your dashboard and process withdrawals.\n\n' \
                       'You can also buy/sell data directly from your GS balance'.format(Decimal(i.plan.daily_earn))
                notifications('Withdrawal Due\n\n'
                              '🤝🤝 Congratulations {}\n\n'
                              '{}\n\n'
                              '{} just getting started ❤❤️'
                              .format(i.user.full_name.title(), mess, site_name),
                              bot_id, group)

            if count >= len(get_today_active_gs):
                print('DONE')
                statistics()
        else:
            print('Value greater than 60k')

def pay_single(email):

    single = UserGold.objects.filter(user__email=email, status='active',
                                          state='approved', next_run_date=date.today())


    print(single)
    get_today_active_gs = single[:1]

    if get_today_active_gs.count() == 0:
        print('NO DATA')
        statistics()
    count = 0

    for i in get_today_active_gs:
        count += 1
        user_wallet = UserWallet.objects.get(user=i.user)
        # check if is end date
        if i.end_date == date.today():
            i.total_earned += Decimal(i.total_left)
            user_wallet.user_balance += Decimal(i.total_left)
            user_wallet.testified = False

            mess = 'Your last GS value  of ₦{:,} has been paid directly into your wallet balance.' \
                   ' Kindly login to your dashboard and process withdrawals.\n\n' \
                   'You can also buy/sell data directly from your GS balance'.format(Decimal(i.total_left))
            notifications('Cheers 🍷🍷 {}\n\n'
                          '{}\n\n'
                          'Thanks for trusting us 🤝🤝,\n\n'
                          'We look forward to see you again as we promise not to fail any of our investors. 👊🏼\n'
                          '{} cares ❤❤️'
                          .format(i.user.full_name.title(), mess, site_name),
                          bot_id, group)

            i.total_left = 0
            i.status = 'ended'
            i.save()
            user_wallet.save()

        else:
            i.total_left -= Decimal(i.plan.daily_earn)
            i.total_earned += Decimal(i.plan.daily_earn)
            user_wallet.user_balance += Decimal(i.plan.daily_earn)
            user_wallet.testified = False

            if i.earn_after == '48':
                i.next_run_date = current_timezone + timedelta(days=2)
            elif i.earn_after == '4days':
                i.next_run_date = current_timezone + timedelta(days=4)
            else:
                i.next_run_date = current_timezone + timedelta(days=1)

            i.save()
            user_wallet.save()

            mess = '🍷 Your daily GS value  of ₦{:,} has been paid directly into your wallet balance.' \
                   'Kindly login to your dashboard and process withdrawals.\n\n' \
                   'You can also buy/sell data directly from your GS balance'.format(Decimal(i.plan.daily_earn))
            notifications('Withdrawal Due\n\n'
                          '🤝🤝 Congratulations {}\n\n'
                          '{}\n\n'
                          '{} just getting started ❤❤️'
                          .format(i.user.full_name.title(), mess, site_name),
                          bot_id, group)

            if count >= len(get_today_active_gs):
                print('DONE')
                statistics()


def open_market():
    admin.site_available = True
    admin.save()

    notifications('✅✅✅ GS Available 🪙🪙\n\n'
                  'This is to officially notify you that GS stock market for {} is currently opened.👊🏼\n\n'
                  '{} Cares ❤️'
                  .format(date.today(), site_name),
                  bot_id, group)

def close_market():
    admin.site_available = False
    admin.save()

    notifications('🚫🚫🚸 Out of GS 🪙🪙 \n\n'
                  'This is to officially notify you that GS stock market for {} is currently closed.👊🏼\n\n'
                  '{} Cares ❤️'
                  .format(date.today(), site_name),
                  bot_id, group)

