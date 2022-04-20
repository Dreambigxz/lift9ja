import transaction_id
from variables import *
from s3 import s3_update
# Create your views here.

class UserDeposit(LoginRequiredMixin, View):

    login_url = '/sign-in'

    def get(self, request):

        Plan = Packages.objects.all()
        deposit_table = WalletHistory.objects.filter(user=self.request.user)

        table = WalletHistory.objects.filter(user=self.request.user, type='deposit')

        paginator = Paginator(table, 5)
        page_number = request.GET.get('page')
        get_user_table = paginator.get_page(page_number)


        return render(request, 'wallet/deposit.html',
                      {
                          'history': get_user_table,
                          'plan': Plan

                      })

    def post(self, request):

        try:

            deposit_type = request.POST['type']
            amount = request.POST['amount']
            get_user_deposit_value = Decimal(amount)

            admin_bank = AdminBank.objects.get(id=1)

            # if deposit_type == 'transfer':
            #     """
            #     get bank details
            #     """
            #     # if int(get_user_deposit_value) in range(100, 101000):
            #     #
            #     #     name = request.user.username
            #     #     user_id = request.user.id
            #     #     email = request.user.email
            #     #     user_deposit_id = deposit_id()
            #     #
            #     #     # call deposit api function
            #     #     print(get_user_deposit_value)
            #     #     datas = transfer_deposit(tx_ref=user_deposit_id,
            #     #                              amount=(get_user_deposit_value),
            #     #                              email=email,
            #     #                              currency='NGN')
            #     #
            #     #     # return the payment link for the user to complete his deposit
            #     #
            #     #     account_number = (datas['meta']['authorization']['transfer_account'])
            #     #     bank = (datas['meta']['authorization']['transfer_bank'])
            #     #     amount = (datas['meta']['authorization']['transfer_amount'])
            #     #
            #     #     print(account_number, bank, amount)
            #     #     data['success'] = account_number, bank, amount
            #     #
            #     #     messages.success(request, '{} '
            #     #                               'Copy the details below to complete your digital wallet deposit. Please Dont reload or leave this page for now.'.format(success),
            #     #                      )
            #     #
            #     #     return render(request, 'wallet/deposit.html',
            #     #       {
            #     #           'account_number': account_number,
            #     #           'bank': bank,
            #     #           'amount': amount,
            #     #           'message': 'Account Found',
            #     #           'Bank': 'Bank',
            #     #           'AccountNumber': 'Account Number',
            #     #           'Amount': 'Amount',
            #     #       })
            #
            #
            #     if int(get_user_deposit_value) in range(minimum, maximum):
            #
            #         username = request.user.username
            #         user_id = request.user.id
            #         email = request.user.email
            #         user_deposit_id = deposit_id()
            #
            #         messages.success(request, '{} '
            #                                   'Copy the details below to complete your peek wallet deposit. Please do not reload this page for now or you screenshot the details.'.format(success),
            #                          )
            #
            #         warning = 'Please only put your username as the payment note.'
            #         return render(request, 'wallet/deposit.html',
            #
            #           {
            #               'account_number': admin_bank.account_number,
            #               'bank': admin_bank.bank_name,
            #               'amount': get_user_deposit_value,
            #               'name': admin_bank.account_name,
            #               'message': 'Account Found',
            #               'Bank': 'Bank',
            #               'AccountNumber': 'Account Number',
            #               'Amount': 'Amount',
            #               'AccountName': 'Account Name',
            #               'warning': warning,
            #               'copy': True
            #           })
            #
            #     else:
            #         messages.info(request, 'Minimum of {:,} and maximum of {:,} naira required per transaction.'.format(
            #             minimum, maximum
            #         ))
            #         return redirect('/buy-coupon')
            #
            # elif deposit_type == 'Card':
            #     if int(get_user_deposit_value) in range(50, 101000):
            #         name = request.user.username
            #         user_id = request.user.id
            #         current_site = get_current_site(request)
            #         email = request.user.email
            #         user_deposit_id = deposit_id()
            #
            #         # call deposit api function
            #         link = deposit_api(tx_ref=user_deposit_id, amount=int(get_user_deposit_value),
            #                            name=name, user_id=user_id, email=email, currency='NGN', current_site=current_site)
            #
            #         # return the payment link for the user to complete his deposit
            #
            #         data['success'] = link
            #         return redirect(link)
            #
            #     else:
            #         messages.info(request, 'Minimum of ₦1,000 and maximum ₦100,000 per transaction required for card deposit.')
            #         return redirect('/buy-coupon')

            if deposit_type == 'vendor':
                """
                get bank details
                """

                # messages.success(request, '{} '
                #                           'Copy the details below to complete your peek wallet deposit. Please do not reload this page for now or you screenshot the details.'.format(success),
                #                  )

                warning = 'Please only contact numbers available here for your coupon code after or before payment.'
                return render(request, 'wallet/deposit.html',

                  {
                      'account_number': admin_bank.account_number,
                      'bank': admin_bank.bank_name,
                      'amount': get_user_deposit_value,
                      'name': admin_bank.account_name,
                      'message': 'Vendors Found (1)',
                      'Bank': 'Bank',
                      'AccountNumber': 'Account Number',
                      'Amount': 'Amount',
                      'AccountName': 'Account Name',
                      'Whatsapp': 'Whatsapp number',
                      'wanumber': '+2348077150253',
                      'warning': warning,
                      'copy': True
                  })

        except:
            messages.error(request, 'Make sure all fields are selected.')
            return redirect('/buy-coupon')

class UpdateCouponCode(LoginRequiredMixin, View):
    login_url = '/sign-in'

    def get(self, request):
        return render(request, 'wallet/update-coupon.html')
    def post(self, request):

        code = request.POST['code']

        # load file
        new_list = load_file(file_name)

        # check if user supplied details exist
        if code in new_list:
            (s3_update(code))
            packages_range = {
                '5kc': '5000',
                '10k': '10000',
                '15k': '15000',
                '20k': '20000',
                '30k': '30000',
                '40k': '40000',
                '50k': '50000',
                '60k': '60000',
                '70k': '70000',
                '80k': '80000',
                '90k': '90000',
                '100': '100000',
                '200': '200000',
                '300': '300000',
                '400': '400000',
                '500': '500000',
            }

            get_package = code[:3]
            package = packages_range[get_package]

            # credit the user wallet
            wallet = UserWallet.objects.get(user=self.request.user)
            wallet.user_balance += Decimal(package)
            wallet.save()

            WalletHistory.objects.create(user=self.request.user,
                                         amount=Decimal(package),
                                         transaction_id=get_transaction_id(),
                                         tx_ref=code,
                                         type='deposit',
                                         status='success',
                                         date=current_timezone,
                                        )

            messages.info(request, "Coupon code valid, you have successfully added ₦{:,} to your wallet, kindly click the buy button to start buying shares now.".format(Decimal(package)))
            return redirect('/buy-shares')

        else:

            messages.error(request, 'Coupon code not valid, please purchase a valid code and try again.')
            return redirect('/update-coupon')

@require_GET
@login_required
def process_deposit(request):
    try:
        status = request.GET['status']

        if status == 'successful':

            transaction_id = request.GET['transaction_id']

            #call transaction verification function
            #to verify user transaction
            verify_user = verify_transanction(transaction_id=transaction_id)

            get_transaction_status = verify_user['status']
            get_transaction_id = verify_user['data']['id']
            get_deposit_amount = verify_user['data']['charged_amount']
            get_tx_ref_num = verify_user['data']['tx_ref']
            user = verify_user['data']['customer']['email']

            """
            Start neccessary check and update ##Daniel be carefull cos u can do it
            """
            #check fluter endpoint transaction status after verification
            if get_transaction_status == 'success':



                #check if transaction_id and tx_ref number has exist
                user= MyUser.objects.get(email=user)

                if WalletHistory.objects.filter(user=user,
                                                 transaction_id=get_transaction_id,
                                                 tx_ref=get_tx_ref_num,
                                                 status='success').exists():

                    return redirect('/')

                else:
                    user_amount_to_deposit = "N{:,}".format(int(get_deposit_amount))
                    print(user_amount_to_deposit)

                    messages.info(request, 'Your  deposit request has been submitted. '
                                              'Awaiting for confirmation. '
                                              'You can check the deposit record in a short while.')
                    return redirect('wallet:user_deposit')

        elif status == 'cancelled':
            tx_ref = request.GET['tx_ref']

            if WalletHistory.objects.filter(user=request.user,
                                             tx_ref=tx_ref,
                                             status='success').exists():

                messages.info(request, 'Your  deposit request has been submitted,'
                                       'awaiting for confirmation. '
                                       'You can check the deposit record in a short while. Send us a message if it fails to reflect after 10mins')
                return redirect('/deposot')

            else:
                print('cancelled')
                messages.info(request, 'If your transaction was successful, your wallet will be credited within a few minutes. Send us a message if it fails to reflect after 10mins.')
                return redirect('/buy-coupon')

    except:
        return redirect('/buy-coupon')

@require_POST
@csrf_exempt
def deposit_webhook(request):

    notifications('WEBHOOK IS WORKING', bot_id, support)

    webhook_body = (request.body)
    decode_body = webhook_body.decode('utf-8')
    cvt_to_dict = json.loads(decode_body)

    notifications(cvt_to_dict, bot_id, support)

    hash = request.headers["verif-hash"]

    if hash == settings.FLUTTER_WAVE_HASH_KEY:

        status = cvt_to_dict['data']['status']
        if status == 'successful':

            # call transaction verification function
            # to verify user transaction
            get_transaction_status = cvt_to_dict['data']['status']
            get_transaction_id = cvt_to_dict['data']['id']
            get_deposit_amount = cvt_to_dict['data']['amount']
            get_tx_ref_num = cvt_to_dict['data']['tx_ref']
            user = cvt_to_dict['data']['customer']['email']

            user = MyUser.objects.get(email=user)

            """
            Start necessary check and update 
            """
            # check flutter endpoint transaction status after verification
            if get_transaction_status == 'successful':

                # check if transaction_id and tx_ref number has exist
                if WalletHistory.objects.filter(user=user,
                                                transaction_id=get_transaction_id,
                                                tx_ref=get_tx_ref_num, status='success').exists():

                    return redirect('/')

                else:


                    # befor updateing the user table, check if he is trying to
                    # upgrade his account and charge account upgrade

                    get_user_deposit_value = get_deposit_amount

                    # if get_user_deposit_value - 57 in range(1000, 3000):
                    #
                    #     deposit_charge = 57
                    #     print(deposit_charge)
                    #
                    #     get_deposit_amount = get_deposit_amount - deposit_charge
                    #
                    #     admin.deposit_earning += deposit_charge
                    #     admin.save()
                    #
                    #     UserWallet.objects.filter(user=user).update(get_first_deposit=True,
                    #                                                 user_balance=
                    #                                                 F('user_balance') +
                    #                                                 int(get_deposit_amount))
                    #
                    # elif get_user_deposit_value - 157 in range(3000, 10000):
                    #
                    #     deposit_charge = 157
                    #
                    #     print(deposit_charge)
                    #
                    #     get_deposit_amount = get_deposit_amount - deposit_charge
                    #
                    #     admin.deposit_earning += deposit_charge
                    #     admin.save()
                    #
                    #     UserWallet.objects.filter(user=user).update(get_first_deposit=True,
                    #                                                 user_balance=
                    #                                                 F('user_balance') +
                    #                                                 int(get_deposit_amount))
                    #
                    # elif get_user_deposit_value - 257 in range(10000, 50000):
                    #
                    #     deposit_charge = 257
                    #     print(deposit_charge)
                    #
                    #     get_deposit_amount = get_deposit_amount - deposit_charge
                    #
                    #     admin.deposit_earning += deposit_charge
                    #     admin.save()
                    #
                    #     UserWallet.objects.filter(user=user).update(get_first_deposit=True,
                    #                                                 user_balance=
                    #                                                 F('user_balance') +
                    #                                                 int(get_deposit_amount))
                    #
                    # elif get_user_deposit_value - 357 in range(50000, 100001):
                    #
                    #     deposit_charge = 357
                    #     print(deposit_charge)
                    #
                    #     get_deposit_amount = get_deposit_amount - deposit_charge
                    #
                    #     admin.deposit_earning += deposit_charge
                    #     admin.save()
                    #
                    #     UserWallet.objects.filter(user=user).update(get_first_deposit=True,
                    #                                                 user_balance=
                    #                                                 F('user_balance') +
                    #                                                 int(get_deposit_amount))

                    # create history table
                    """
                    handling stamp charge
                    """
                    if get_deposit_amount in range(10000, 500000):
                        WalletHistory.objects.create(user=user,
                                                     amount=get_deposit_amount,
                                                     transaction_id=get_transaction_id,
                                                     tx_ref=get_tx_ref_num,
                                                     type='deposit',
                                                     status='success',
                                                     stamp_charge=50,
                                                     date=current_timezone
                                                     )

                    else:
                        WalletHistory.objects.create(user=user,
                                                     amount=get_deposit_amount,
                                                     transaction_id=get_transaction_id,
                                                     tx_ref=get_tx_ref_num,
                                                     type='deposit',
                                                     status='success',
                                                     date=current_timezone
                                                     )


                    UserWallet.objects.filter(user=user).update(get_first_deposit=True,
                                                                user_balance=
                                                                F('user_balance') +
                                                                int(get_deposit_amount))


                    # cal_deposite = percentage_calculator(percent=1.4, amount=float(get_deposit_amount))
                    #
                    # admin.charges_beared += cal_deposite
                    # # admin.save()
                    #
                    # daily_limit = TotalFundingToday.objects.get(id=1)
                    #
                    # """
                    #   check if daily limit  date is greater than 24hours
                    # """
                    #
                    # current_date = utc.localize(datetime.datetime.now() + timedelta(hours=1))
                    # limit_date = daily_limit.datetime

                    # if limit_date <= current_date:
                    #     # clear daily_funding abd change date to todaydaily_limit.datetime + timedelta(days=1, hours=1)
                    #     daily_limit.amount = 0
                    #     daily_limit.datetime = daily_limit.datetime + timedelta(days=1)
                    #     daily_limit.save()
                    #
                    # # add funding to total daily limit)
                    #
                    # daily_limit.amount += Decimal(get_deposit_amount)
                    # daily_limit.save()
                    #
                    # # record stamp charge

                    return redirect('/welcome')

    else:
        # invalid request
        return redirect('/')

class UserWalletWithdrawal(LoginRequiredMixin, View):
    login_url = '/sign-in'

    def get(self, request):

        deposit_table = WalletHistory.objects.filter(user=self.request.user)
        table = WalletHistory.objects.filter(user=self.request.user, type='withdraw')
        user_wallet = UserWallet.objects.get(user=self.request.user)

        if user_wallet.testified == False:
            return redirect('/testify')

        paginator = Paginator(table, 5)
        page_number = request.GET.get('page')
        get_user_table = paginator.get_page(page_number)

        return render(request, 'wallet/withdrawal.html',
                      {
                          'history': get_user_table
                      })

    def post(self, request):

        amount = request.POST['amount']
        account_number = request.POST['account_number']
        bank_code = request.POST['bank-code']
        bank_name = request.POST['bankName']
        pin = request.POST['pin']

        user_wallet = UserWallet.objects.get(user=self.request.user)
        preference = UserPreference.objects.get(user=self.request.user)
        amount = Decimal(amount)

        """
        Validations
        """
        #
        # if user_wallet.testified == False:
        #     messages.info(request, 'Add a testimony to continue with your withdrawal request.')
        #     return redirect('/testify')

        #staff check
        # if self.request.user.staff == True:
        #     messages.info(request, "User is staff")
        #     return redirect('/updatePayment')

        # balance check
        if amount > user_wallet.user_balance:
            messages.info(request, 'Your withdrawal amount is greater than your wallet balance')
            return redirect('/withdraw')

        elif WithdrawPin.objects.filter(user=request.user, pin=pin).exists():
            pass
        else:
            messages.info(request, 'Incorrect withdrawal pin provided, please try again or contact support.')
            return redirect('/withdraw')

        #minimum
        if amount < minimum_withdrawal:
            messages.info(request, 'Minimum withdrawal is ₦100.')
            return redirect('/withdraw')

        try:

            review = WithdrawReview.objects.get(user=request.user)
            review.beneficiary = request.user.full_name
            review.bank_code = bank_code
            review.amount = amount
            review.bank_name = bank_name
            review.account_number = account_number
            review.time_updated = current_timezone
            review.active = True
            review.save()
        except:
            WithdrawReview.objects.get_or_create(user=request.user,
                                                 beneficiary=request.user.full_name,
                                                 bank_code=bank_code,
                                                 amount=amount,
                                                 bank_name=bank_name,
                                                 account_number=account_number,
                                                 active=True,
                                                 time_updated=current_timezone
                                                 )

        messages.info(request,
                      "Please review your account details and continue.")

        return render(request, 'wallet/withdrawal.html', {
            'beneficiary': request.user.full_name,
            'verified': True,
            'bank_code': bank_code,
            'amount': amount,
            'bank_name': bank_name,
            'account_number': account_number,

        })


@login_required
def process_withdraw(request):
    if request.method == 'POST':

        review = WithdrawReview.objects.get(user=request.user)
        user_wallet = UserWallet.objects.get(user=request.user)

        """
        PASS TEST PENDING
        """
        if review.active != True:
            messages.error(request, 'An error occurred, please try again.')
            return redirect('/withdraw')

        if Decimal(review.amount) > user_wallet.user_balance:
            messages.info(request, 'Your withdrawal amount is greater than your wallet balance')
            return redirect('/withdraw')
            #        AND DEDUCT USERS WALLET

        user_wallet.user_balance -= Decimal(review.amount)
        # user_wallet.testified = False
        # user_wallet.to_cash_out = False
        user_wallet.save()
        review.active = False
        review.save()

        WalletHistory.objects.create(user=request.user,
                                     wallet=user_wallet,
                                     type='withdraw',
                                     status='pending',
                                     transaction_id=get_transaction_id(),
                                     amount=review.amount,
                                     account_number=review.account_number,
                                     bank_name=review.bank_name,
                                     bank_code=review.bank_code,
                                     date=current_timezone
                                     )

        # send a message to the withdrawal admin
        public_group_notification('NEW WITHDRAWAL REQUEST\n'
                                 'View page: https://goldstockng.com/pending-payment\n\n'
                                 'account_number: {}\n'
                                 'amount:  ₦{:,}\n'
                                 'bank {}\n'
                                 'user : {}'.format(review.account_number, Decimal(review.amount),
                                                    review.bank_name, review.user.full_name.title()),
                                 bot_id, payment_grp
                        )

        # send to general group
        notifications('🤝🤝 Congratulations {} !!!\n\n'
                                 'Your ₦{:,} withdrawal request has been submitted and being process, you will be notify immediately is sent within the next 24hrs.\n\n'
                                 'Best Regards, {}.'.format(review.user.full_name.title(),
                                                            Decimal(review.amount), site_name),
                                 bot_id, group
                                 )

        messages.success(request, '{} Withdraw successfully submitted.'
                                  'Payment frame is currently within 24hrs'.format(success))
        return redirect('/withdraw')

class ChangePin(LoginRequiredMixin, View):
    login_url = '/sign-in'

    def get(self, request):

        return render(request, 'wallet/pin.html')

    def post(self, request):

        old_pin = request.POST['old_pin']
        new_pin = request.POST['new_pin']

        if len(new_pin) < 4:
            messages.info(request, 'Minimum of 4 didgit required.')
            return redirect('wallet:changePin')

        user_pin = WithdrawPin.objects.get(user=self.request.user)

        if user_pin.pin == old_pin:
            user_pin.pin = new_pin
            user_pin.save()

            messages.success(request, 'Pin successfully changed.')
            return redirect('wallet:changePin')
        else:
            messages.info(request, 'Incorrect old pin provided.')
            return redirect('wallet:changePin')
