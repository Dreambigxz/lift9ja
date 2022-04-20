from variables import *

def global_variables(request):

    if request.user.is_authenticated:

        wallet = UserWallet.objects.get(user=request.user)

        if request.user.is_admin == True:
            contact = MyContacts.objects.filter()
            total_deposit = WalletHistory.objects.filter(type='deposit')
            sum_total_deposit = sum([i.amount for i in total_deposit])
        else:
            contact = MyContacts.objects.filter(user=request.user)
            total_deposit = WalletHistory.objects.filter(user=request.user, type='deposit')
            sum_total_deposit = sum([i.amount for i in total_deposit])

        mtn_cg = CgWallet.objects.get(network='12')

        return {
            'number': "+2348167997730",
            'address': 'address',
            'email': 'help@palmgig.com',
            'sitename': 'Palm Gig Limited',

            'account_number1': '43324903015',
            'bank1': 'FCMB',

            'account_number2': '43324903015',
            'bank2': 'UBA',

            'wallet': wallet,
            'count_contacts': contact.count(),
            'count_total_deposit': total_deposit.count(),
            'sum_total_deposit': sum_total_deposit,

            'mtn': conv_MB_to_GB(mtn_cg.data_balance),
            'mtn_val': mtn_cg.val,
            'data_balance': mtn_cg.data_balance

        }

    else:

        return {
            'number': "+2348167997730",
            'address': 'address',
            'email': 'help@palmgig.com',
            'sitename': 'Palm Gig Limited',
        }