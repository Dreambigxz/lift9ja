import time
import datetime
from variables import *

# Create your views here.
class MyAdmin(LoginRequiredMixin, View):
    login_url = '/sign-in'

    def get(self, request):

        if self.request.user.staff:

            staffs = MyUser.objects.filter(staff=True).count()

            pending_withdrawal = WalletHistory.objects.filter(type='withdraw',
                                                               status='pending').count()

            total_deposit_amount = sum([i.amount for i in WalletHistory.objects.filter(type='deposit', status='success').exclude(user__staff=True)])
            count_total_deposit = WalletHistory.objects.filter(type='deposit', status='success').exclude(user__staff=True).count()
            count_total_withdrawal = WalletHistory.objects.filter(type='withdraw', status='success').exclude(user__staff=True).count()
            total_withdrawal_amount = sum([i.amount for i in WalletHistory.objects.filter(type='withdraw', status='success').exclude(user__staff=True)])


            total_users = MyUser.objects.all().exclude(staff=True).count()
            active_users = MyUser.objects.filter(is_active=True).exclude(staff=True).count()

            total_investors_count = Subscibers.objects.all().exclude(user__staff=True).count()

            total_running_investment_amount = sum([i.total_earned for i in Subscibers.objects.filter(status='active').exclude(user__staff=True)])
            total_running_investment_count = Subscibers.objects.filter(status='active').exclude(user__staff=True).count()

            # bill = admin.bill_settlement_fake
            bill = admin.bill_settlement

            total_balance = total_deposit_amount - total_withdrawal_amount - bill


            return render(request, 'admin/admin.html', {

                'staffs': staffs,
                'pending_withdrawal': pending_withdrawal,
                'total_deposit_amount': total_deposit_amount,
                'count_total_deposit': count_total_deposit,
                'count_total_withdrawal': count_total_withdrawal,
                'total_withdrawal_amount': total_withdrawal_amount,
                'total_investors_count': total_investors_count,
                'total_running_investment_amount': total_running_investment_amount,
                'total_running_investment_count': total_running_investment_count,
                'total_users': total_users,
                'active_users': active_users,
                'total_balance': total_balance,
                'bill': bill
            })
        else:
            return redirect('/')

class UpdatePayment(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.is_staff == True:

            pending_gs_purchase = UserGold.objects.filter(status='pending', state='awaiting approval', subscribed_date__gte=date.today())

            try:
                user_id = request.GET['id']

                get_gs = UserGold.objects.get(id=user_id)
                get_gs.delete()
                messages.success(request, "{} User GS deleted".format(success))
                return redirect('/updateUserGoldStock')

            except:
                pass

            return render(request, 'admin/alertify/update-payment.html',
                          {
                              'data': pending_gs_purchase
                          })
        else:
            return redirect('/')

    def post(self, request):

        user_id = request.POST['user_id']
        amount = Decimal(request.POST['amount'])

        try:
            get_gs = UserGold.objects.get(id=user_id, state='awaiting approval')
        except:
            messages.info(request, "User Already approved")
            return redirect('/updateUserGoldStock')


        if amount == get_gs.plan.amount:

            if UserGold.objects.filter(user__email=get_gs.user.email, state='approved').exists():
                pass
            else:
                pass

            try:
                referred_by = UserReferral.objects.get(referred__email=get_gs.user.email)
            except:
                referred_by = UserReferral.objects.create(referred=get_gs.user,
                                                          user=MyUser.objects.get(email='donyemordi@gmail.com'))
            # if referred_by.active == False:
            referred_by.active = True
            if referred_by.withdrawn == True:
                referred_by.earn = percentage_calculator(3, amount)
                referred_by.withdrawn = False
            else:
                referred_by.earn += percentage_calculator(3, amount)
            referred_by.save()

            notifications('👫👫 Referral Bonus Alert\n\n'
                          '🤝🤝 Congratulations {}\n\n'
                          'Your referral bonus of ₦{:,} has been sent to your account.\n\n'
                          'Keep up the good work. 💥💥'
                          .format(referred_by.user.full_name.title(), percentage_calculator(3, amount)),
                          bot_id, group)

            get_gs.state = 'approved'
            get_gs.end_date = current_timezone + timedelta(days=4)
            get_gs.subscribe_date = current_timezone
            get_gs.status = 'active'
            get_gs.total_left = get_gs.plan.total_earn
            if get_gs.earn_after == '48':
                get_gs.next_run_date = current_timezone + timedelta(days=2)
            elif get_gs.earn_after == '4days':
                get_gs.next_run_date = current_timezone + timedelta(days=4)
            else:
                get_gs.next_run_date = current_timezone + timedelta(days=1)
            get_gs.save()

            try:

                gs_mess = "Your purchase of {} worth of Gold Stock 🪙🪙 of N{:,} has been confirmed, and your plan has been activated automatically.\n\n\
                           kindly click on My Gold button to track your active Gold Stocks.".format(
                    get_gs.plan.plan, get_gs.plan.amount
                )

                notifications('🤝🤝Congratulations {}\n\n'
                              '{}\n\n'
                              'GS Stock Cares. ❤️'
                              .format(get_gs.user.full_name.title(), gs_mess),
                              bot_id, group)
            except:
                pass

            messages.success(request, "{} ₦{:,} Gold created.".format(success, amount,))
            return redirect('/updateUserGoldStock')

        else:
            messages.info(request, "Make sure amount seen is equall to GS bought amount")
            return redirect('/updateUserGoldStock')

def get_live_update_view(request):

    bill = admin.bill_settlement

    users = MyUser.objects.all().count()
    active_gs_count = UserGold.objects.filter(state='approved').exclude(user__is_admin=True).count()
    all_gs_count = UserGold.objects.filter().count()

    active_gs_bought = sum([i.plan.amount for i in UserGold.objects.filter(state='approved').exclude(user__is_admin=True)])
    all_gs = sum([i.plan.amount for i in UserGold.objects.filter()])

    total_withdrawal_amount = sum([i.amount for i in WalletHistory.objects.filter(type='withdraw', status='success').exclude(user__is_admin=True)])


    balance = active_gs_bought - total_withdrawal_amount -  bill


    notifications('LIVE UPDATES  !!!\n\n'
                             'Active GS: {} \n'
                             'GS Purchase: ₦{:,} \n'
                             'Total Withdrawal ₦{:,} \n\n'
                             'Total Bill Settled ₦{:,} \n\n'
                  
                             'Total Balance ₦{:,}\n'
                             'Total users: {:,}\n'.format(active_gs_count, active_gs_bought,
                                                          total_withdrawal_amount, bill,
                                                          balance, users),
                                                           bot_id, '-649094803')

    messages.success(request, 'Successfully sent live update')
    return redirect('/my-gs-data')

class PendingPayment(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_admin:

            withdrawal = WalletHistory.objects.filter(type='withdraw',
                                                      status='pending').exclude(user__staff='True').order_by('date')

            pending_withdrawal = WalletHistory.objects.filter(type='withdraw',
                                                      status='pending').exclude(user__staff='True')

            total = sum([i.amount for i in pending_withdrawal])
            return render(request, 'admin/alertify/pending-payment.html',
                          {
                              'withdrawal': withdrawal,
                              'count_withdrawal': pending_withdrawal.count(),
                              'pending_withdrawal': total,
                          })

        else:
            return redirect('/')

def process_payment_view(request):

    if request.user.is_admin:

        user = request.GET['user_id']

        user_wallet_history = WalletHistory.objects.get(id=user)

        get_full_name = user_wallet_history.user.full_name

        #call flutter api to send the moneypending_to_receive_today

        if user_wallet_history.status == 'pending':

            user_wallet_history.status = 'success'
            user_wallet_history.save()

            notifications('♻️🟢💳 {} Payment Dispatched\n\n'
                          'Gold Stock Payment To !!!\n\n'
                                     
                             'NAME:: {} \n'
                             'Amount ₦{:,}: \n'
                             'BANK: {}\n\n'
                          
                          'This is to notify you that payment has been dispatched to the above account.\n'
                          'Do well by sharing testimonies.\n\n'
                           'Thanks for trusting us.'.format(site_name,
                                                             get_full_name.title(),
                                                             user_wallet_history.amount,
                                                             user_wallet_history.bank_name.title()),
                                                              bot_id, group)

            messages.success(request, 'Transaction completed')
            return redirect('/pending-payment')

def auto(request):
    if request.user.is_admin:

        user = request.GET['user_id']

        user_wallet_history = WalletHistory.objects.get(id=user)

        get_full_name = user_wallet_history.user.full_name

        # try:
        if user_wallet_history.user.is_admin == True:
            user_wallet_history.status = 'success'
            user_wallet_history.save()

            notifications('♻️🟢💳 {} Payment Dispatched\n\n'
                          'Gold Stock Payment To !!!\n\n'

                          'NAME:: {} \n'
                          'Amount ₦{:,}: \n'
                          'BANK: {}\n\n'

                          'This is to notify you that payment has been dispatched to the above account.\n'
                          'Do well by sharing testimonies.\n\n'
                          'Thanks for trusting us.'.format(site_name,
                                                           get_full_name.title(),
                                                           user_wallet_history.amount,
                                                           user_wallet_history.bank_name.title()),
                          bot_id, group)

            messages.success(request, 'Admin withdrawal Notified')
            return redirect('/pending-payment')

        if user_wallet_history.status == 'pending':
            transfer_api = withdraw(amount=float(user_wallet_history.amount),
                                    account_number=user_wallet_history.account_number,
                                    account_bank=user_wallet_history.bank_code,
                                    user=get_full_name,
                                    mac_id=get_transaction_id())

            if transfer_api['status'] == 'success':

                user_wallet_history.status = 'success'
                user_wallet_history.save()

                try:

                    notifications('{} Payment Dispatched\n\n'
                                  'Gold Stock Payment To !!!\n\n'

                                  'NAME:: {} \n'
                                  'Amount ₦{:,}: \n'
                                  'BANK: {}\n\n'

                                  'This is to notify you that payment has been dispatched to the above account.\n'
                                  'Do well by sharing testimonies.\n\n'
                                  'Thanks for trusting us.'.format(site_name,
                                                                   get_full_name.title(),
                                                                   user_wallet_history.amount,
                                                                   user_wallet_history.bank_name.title()),
                                  bot_id, group)
                except:
                    pass

                messages.success(request, 'Successfully Queued up for transfer')
                return redirect('/pending-payment')

            elif transfer_api['message'] == 'Transfer creation failed':
                messages.error(request,
                               'Account verification failed. Please contact user or try again later.')
                return redirect('/pending-payment')

            else:
                messages.error(request, 'Please try again letter')
                return redirect('/pending-payment')

                # try:
                #
                # except:
                #
                #     messages.error(request, 'Unexpected error, try again.')
                #     return redirect('/pending-payment')

        else:
            messages.success(request, 'Transaction completed')
            return redirect('/pending-payment')
        # except:
        #     messages.error(request, 'Unexpected error, try again.')
        #     return redirect('/pending-payment')
    else:
        messages.info(request, 'No page privilege')
        return redirect('/dashboard')

def process_all_withdraw(request):

    emails = ['yusufaiza64@gmail.com', 'gregoryilori02@gmail.com', 'donyemordi@gmail.com']
    if request.user.email in emails:

        user_wallet_history = WalletHistory.objects.filter(status='pending')

        print(user_wallet_history)

        for i in user_wallet_history:
            #call flutter api to send the money
            if i.status == 'pending':
                try:
                    tranfer_api = withdraw(amount=float(i.amount),
                                           account_number=i.account_number,
                                           account_bank=i.bank_code,
                                           user=i.user.full_name,
                                           mac_id=i.id)

                    if tranfer_api['status'] == 'success':
                        i.status = 'success'
                        i.save()

                except:

                    messages.info(request, 'Please try again letter')
                    return redirect('myadmin:admin_dashboard')

            else:
                messages.info(request, 'Transaction completed')
                return redirect('myadmin:admin_dashboard')

        messages.success(request, 'Transfer successfully Queued up for transfer')
        return redirect('myadmin:admin_dashboard')
    else:
        messages.info(request, 'An error occured')
        return redirect('myadmin:admin_dashboard')

@login_required
def change_name(request):
    name = request.POST['name']
    user = MyUser.objects.get(user=request.user)
    user.full_name = name
    user.save()
    messages.info(request, 'Name changed successfully')
    return redirect('myadmin:admin_dashboard')

@login_required
def gs_daily_payment_view(request):

    if request.user.is_admin != True:
        return redirect('/')
    get_today_active_gs = UserGold.objects.filter(status='active', state='approved', next_run_date=date.today())
    print(get_today_active_gs.count())
    get_today_active_gs = get_today_active_gs[:1]

    if get_today_active_gs.count() == 0:
        print('NO DATA')
        return redirect('/')
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
                   ' Kindly login to your dashboard and process withdrawals'.format(Decimal(i.total_left))
            notifications('Cheers 🍷🍷\n\n'
                          '{}\n\n'
                          'Thanks for trusting us 🤝🤝,\n\n'
                          'We look forward to see you again as we promise not to fail any of our investors. 👊🏼\n'
                          '{} cares ❤️'
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
                   ' Kindly login to your dashboard and process withdrawals'.format(Decimal(i.plan.daily_earn))
            notifications('Withdrawal Due\n\n'
                          'Congratulations {}\n\n'
                          '{}\n\n'
                          '{} just getting started❤️'
                          .format(i.user.full_name.title(), mess, site_name),
                          bot_id, group)

        if count >= len(get_today_active_gs):
            print('DONE')
            print(get_today_active_gs.count(), 'LEFT')
            return redirect(ulogin)

@login_required
def statistics(request):

    if request.user.is_admin != True:
        return redirect('/')

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

    today_to_pay = (i.plan.daily_earn for i in get_today_active_gs)
    today_to_pay = sum([today_to_pay, 5600])
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
                          today_to_pay, balance_after_paying),
                  bot_id, private_grp)

    print('Done')

class AddGSVIEW(LoginRequiredMixin, View):
    def get(self, request):
        Plan = Packages.objects.all()


        return render(request, 'admin/add-gs.html',{
            'plan': Plan
        })

    def post(self, request):
        if request.user.is_admin:
            get_email = request.POST['email']
            get_plan = request.POST['plan']
            customize_gs_withdrawal = request.POST['customize_gs_withdrawal']

            plan = Packages.objects.get(id=get_plan)
            # validation
            if MyUser.objects.filter(email=get_email).exists() and Packages.objects.filter(plan=plan).exists():
                # create gs
                user = MyUser.objects.get(email=get_email)

                amount = plan.amount
                get_gs = UserGold.objects.create(user=user,
                                                 plan=plan,
                                                 earn_after=customize_gs_withdrawal
                                                 )

                try:
                    referred_by = UserReferral.objects.get(referred__email=get_gs.user.email)
                except:
                    referred_by = UserReferral.objects.create(referred=get_gs.user,
                                                              user=MyUser.objects.get(email='donyemordi@gmail.com'))
                # if referred_by.active == False:
                referred_by.active = True
                if referred_by.withdrawn == True:
                    referred_by.earn = percentage_calculator(3, amount)
                    referred_by.withdrawn = False
                else:
                    referred_by.earn += percentage_calculator(3, amount)
                referred_by.save()

                notifications('👫👫 Referral Bonus Alert\n\n'
                              '🤝🤝 Congratulations {}\n\n'
                              'Your referral bonus of ₦{:,} has been sent to your account.\n\n'
                              'Keep up the good work. 💥💥 '
                              .format(referred_by.user.full_name.title(), percentage_calculator(3, amount)),
                              bot_id, group)

                get_gs.state = 'approved'
                get_gs.end_date = current_timezone + timedelta(days=4)
                get_gs.subscribe_date = current_timezone
                get_gs.status = 'active'
                get_gs.total_left = get_gs.plan.total_earn
                if get_gs.earn_after == '48':
                    get_gs.next_run_date = current_timezone + timedelta(days=2)
                elif get_gs.earn_after == '4days':
                    get_gs.next_run_date = current_timezone + timedelta(days=4)
                else:
                    get_gs.next_run_date = current_timezone + timedelta(days=1)
                get_gs.save()

                gs_mess = "Your purchase of {} worth of Gold Stock 🪙🪙 of N{:,} has been confirmed, and your plan has been activated automatically.\n\n\
                                       kindly click on My Gold button to track your active Gold Stocks.".format(
                    get_gs.plan.plan, get_gs.plan.amount
                )

                notifications('🤝🤝 Congratulations {}\n\n'
                              '{}\n\n'
                              'GS Stock Cares. ❤️'
                              .format(get_gs.user.full_name.title(), gs_mess),
                              bot_id, group)

                messages.success(request, '{} Success '.format(success))
                return redirect('/add-gs')
            else:
                messages.error(request, 'email does not exist')
                return redirect('/add-gs')

        messages.error(request, 'email does not exist')
        return redirect('/add-gs')