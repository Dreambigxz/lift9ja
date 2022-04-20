from variables import *

def global_variable(request):

        if request.user.is_anonymous:

            return {

                'currency': ' ₦',
                'wallet': '0.0',
                'five_active': 0,
                'siteName': 'GoldStock',
                'email': 'info@woodwest.org',

                'user_subscriptions': 0


            }

        elif request.user.is_authenticated:
            #
            # if UserType.objects.filter(user=request.user).exists():
            #     pass
            # else:
            #     # create User sell price
            #     UserType.objects.create(user=request.user)

            if request.user.is_admin == True:
                # contact = MyContacts.objects.filter()
                total_deposit = WalletHistory.objects.filter(type='deposit')
                sum_total_deposit = sum([i.amount for i in total_deposit])
            else:
                # contact = MyContacts.objects.filter(user=request.user)
                total_deposit = WalletHistory.objects.filter(user=request.user, type='deposit')
                sum_total_deposit = sum([i.amount for i in total_deposit])

            # mtn_cg = CgWallet.objects.get(network='12')

            user_wallet = UserWallet.objects.get(user=request.user)
            five_active = UserReferral.objects.filter(user=request.user)[:99].count()

            try:
                admin_bank = AdminBank.objects.get(id=1)
                admin = Administration.objects.get(user__email='donyemordi@gmail.com')
            except Exception as e:
                admin = ''
                admin_bank = ''

            # messages = AdminMessage.objects.all()


            if five_active >= 99:
                five_active = '99+'

            user_subscriptions = UserGold.objects.filter(user=request.user,
                                                           status='active')[:10].count()


            if user_subscriptions > 9:
                user_subscriptions = '9+'

            return {

                'balance': user_wallet.user_balance,
                'wallet': user_wallet,
                'five_active': five_active,
                'user_subscriptions': user_subscriptions,
                'siteName': 'GoldStock',
                'email': 'info@woodwest.org',
                'admin': admin,

                # 'bank_name': admin_bank.bank_name,
                # 'account_number': admin_bank.account_number,
                # 'account_name': admin_bank.account_name,

                'currency': ' ₦',
                'error': '#d9534f',
                'info': '#5bc0de',
                'success': '#01ddac',
                'today': date.today(),

                'count_total_deposit': total_deposit.count(),
                'sum_total_deposit': sum_total_deposit,

                # vtuApp
                # 'count_contacts': contact.count(),
                # 'mtn': conv_MB_to_GB(mtn_cg.data_balance),
                # 'mtn_val': mtn_cg.val,
                # 'data_balance': mtn_cg.data_balance

            }
