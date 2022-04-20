import time

from variables import *

class IndexView(TemplateView):

    template_name = 'app/index.html'

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):


        if request.user.is_admin == True:
            topUpHistory = TopUpHistory.objects.filter()
            total_expenses = sum([i.amount for i in topUpHistory])

        else:
            topUpHistory = TopUpHistory.objects.filter(user=self.request.user)
            total_expenses = sum([i.amount for i in topUpHistory])

        paginator = Paginator(topUpHistory, 10)
        page_number = request.GET.get('page')
        get_user_table = paginator.get_page(page_number)

        return render(request, 'vtu/dashboard.html', {
            'history': get_user_table,
            'total_expenses': total_expenses
        })

class DataTopUp(LoginRequiredMixin, View):
    def get(self, request):

        old_contacts = MyContacts.objects.filter(user=self.request.user)
        return render(request, 'vtu/data-top-up.html', {
            'contacts': old_contacts
        })

    def post(self, request):
        print("POST DATA FROM CLIENT", request.POST)
        category_id = request.POST['category_id']
        plan_id = request.POST['plan_id']
        contact_opt = request.POST['contact_opt']

        if contact_opt == 'new':
            contact_opt = request.POST['phone_num']

        user_type = UserType.objects.get(user=self.request.user)
        cg_wallet = CgWallet.objects.get(network=category_id)
        cg_data_active = cg_wallet.active
        get_plan = get_all_categories_plan(category_id, user_type.percent, cg_data_active)

        if len(contact_opt) <= 10:
            messages.info(request, 'Please make sure your number is 11 digits without 234, e.g 0816788998')
            return redirect('/data-top-up')

        for data in get_plan:
            if data['id'] == plan_id:
                amount = data['amount']
                plan = data['text']
                get_data_value = data['data_value']
                user_wallet = UserWallet.objects.get(user=self.request.user)

                networks = {

                    '12': 'MTN',
                    '9': '9mobile',
                    '8': 'Airtel',
                    '7': 'Glo'
                }

                def top_up(type):
                    get_message = buy_data(category_id, plan_id, contact_opt)
                    # check if top up was successful and debit the

                    print(get_message)
                    if get_message[
                        'msg'] == 'You do not have sufficient credit in your wallet. Please top-up wallet first':
                        messages.error(request, 'Service error, please try again later')
                        return redirect('/data-to-up')
                    elif list(get_message.keys()).index(
                            'msg') == 0:
                        messages.error(request, get_message['msg'])
                    elif get_message['result'] == 1 and (
                                                            'Data top-up request has been received and will be processed shortly!'
                                                        ) in get_message['msg']:

                        # check if contact exist or add new contact for user
                        if MyContacts.objects.filter(user=self.request.user, contact=contact_opt).exists():
                            pass
                        else:
                            MyContacts.objects.create(user=self.request.user, contact=contact_opt)

                        # create transaction table
                        TopUpHistory.objects.create(
                            user=self.request.user,
                            network=networks[category_id],
                            plan=plan,
                            contact=contact_opt,
                            status='success',
                            date=current_timezone,
                            amount=Decimal(amount)
                        )

                        if type == 'cg_wallet':
                            data_val = conv_GB_to_MB(get_data_value)
                            cg_wallet.data_balance -= float(data_val)
                            cg_wallet.save()

                            user_wallet.user_balance -= Decimal(amount)
                            user_wallet.save()
                        elif type == 'wallet':
                            user_wallet.user_balance -= Decimal(amount)
                            user_wallet.save()

                        messages.success(request, get_message['msg'])
                        return redirect('/data-top-up')

                    else:
                        messages.error(request, 'Service error, please try again later')
                        return redirect('/data-top-up')

                if cg_data_active == True:

                    #check if giveaway is still active
                    if admin.data_gifting == True:
                        #chck capability
                        if UserGold.objects.filter(user=self.request.user, status='active').exists():
                            print(
                                'Data value', get_data_value
                            )

                            # if int(get_data_value) == 500:
                            #     messages.error(request, '500mb plan service not available, please choose another plan or try again later.')
                            #     return redirect('/data-top-up')

                            if int(get_data_value) != 1:
                                messages.info(request, 'Please only select the 1gig offer.')
                                return redirect('/data-top-up')

                            #check number
                            if MyContacts.objects.filter(contact=contact_opt).exists():
                                messages.info(request, 'This number has been rewarded. Note, it can only be once.')
                                return redirect('/data-top-up')

                                                         # dont debit the user
                                                         # check value of data and amount

                            if conv_MB_to_GB(cg_wallet.data_balance) >= float(get_data_value):
                                 top_up('cg_wallet')
                                 mess = 'Dear Customer, You have received 1Gb valid till {}.\n' \
                                        'Thank you.'.format(timezone.now() + timedelta(
                                     days=31
                                 ))

                                 notifications('Free Data Gifting !!!\n\n'
                                               '{} \n\n'
                                               ''
                                               'Data left: {}GB\n\n'
                                               'Proudly sponsored by Delight Data Company'
                                               .format(mess, conv_MB_to_GB(cg_wallet.data_balance)),
                                               bot_id, group)
                            else:
                                 messages.error(request, 'Free data no loner availavle, plase come back in the evening. Site officailicalyy starting tomorrow.')
                                 return redirect('/data-top-up')
                        else:
                            messages.error(request, 'You are not eligible to this offer. Please activate a GS value and try again.')
                            return redirect('/data-top-up')

                    elif user_wallet.user_balance >= Decimal(amount):
                        if conv_MB_to_GB(cg_wallet.data_balance) >= float(get_data_value):

                            messages.error(request, 'Cannot use this service at the moment')
                            return redirect('/data-top-up')
                            top_up('cg_wallet')

                            if get_data_value == 500:
                                data = '500MB'
                            else:
                                data = '{}GB'.format(get_data_value)

                            mess = 'Dear Customer, You have received {} valid till {}.\n' \
                                   'Thank you.'.format(data,
                                                       timezone.now() + timedelta(days=31
                            ))

                            notifications('DDC data purchase successful !!!\n\n'
                                          '{} \n\n'
                                          ''
                                          'Proudly sponsored by Delight Data Company'
                                          .format(mess, conv_MB_to_GB(cg_wallet.data_balance)),
                                          bot_id, group)
                        else:
                            messages.error(request, 'Cannot use this service at the moment')
                            return redirect('/data-top-up')
                    else:
                        messages.error(request,
                                       'You do not have sufficient credit in your wallet. Please top-up wallet first')
                        return redirect('/data-top-up')

                else:
                    if user_wallet.user_balance >= Decimal(amount):
                        messages.error(request, 'Cannot use this service at the moment')
                        return redirect('/data-top-up')
                        top_up('wallet')
                        mess = 'Dear Customer, You have received {} valid till {}.\n' \
                               'Thank you.'.format(data,
                                                   timezone.now() + timedelta(days=31
                                                                              ))
                        notifications('DDC data purchase successful !!!\n\n'
                                      '{} \n\n'
                                      ''
                                      'Proudly sponsored by Delight Data Company'
                                      .format(mess, conv_MB_to_GB(cg_wallet.data_balance)),
                                      bot_id, group)
                    else:
                        messages.error(request, 'You do not have sufficient credit in your wallet. Please top-up wallet first')
                        return redirect('/data-top-up')

        return redirect('/data-top-up')

class GetPlanView(LoginRequiredMixin, View):
    def get(self, request):
        plan = request.GET['plan']
        user_type = UserType.objects.get(user=self.request.user)
        cg_data = CgWallet.objects.get(network=plan)
        cg_data_active = cg_data.active
        data = get_all_categories_plan(plan, user_type.percent, cg_data_active)
        return JsonResponse(data, status=200, safe=False)

def delete_user_top_up_data(request):

    data = request.GET['data']
    data = TopUpHistory.objects.get(user=request.user, id=data)
    data.delete()
    messages.success(request, 'Data history successfully deleted.')
    return redirect('/dcc-dashboard')

