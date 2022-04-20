from variables import *
from templates import *
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, indexView)

class AboutUs(View):

    def get(self, request):

        return render(request, 'lift9ja/about.html')

class Faq(View):

    def get(self, request):

        return render(request, 'lift9ja/faqs.html')

class PrivacyPolicy(View):

    def get(self, request):

        return render(request, 'lift9ja/privacy.html')

class Contact(View):

    def get(self, request):

        return render(request, 'lift9ja/contact.html')

    def post(self, request):

        # try:
            try:
                telegram_username = request.POST['telegram_username']

            except:
                telegram_username = 'None'


            email = request.POST['email']
            fullname = request.POST['fullname']
            message = request.POST['message']


            ContactUs.objects.create(
                name=fullname,
                email=email,
                message=message,
                telegram_username=telegram_username
            )

            try:

                public_group_notification('NEW CONATCT MESSAGE\n'
                              'Full Name: {}\n'
                              'Email Address: {}\n'
                              'Telegram Username @{}\n'
                              'Message : {}'.format(fullname, email, telegram_username, message),
                              bot_id, support)
            except:
                pass

            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": settings.EMAIL_DELIVERY,
                            "Name": 'CONATCT US'
                        },
                        "To": [
                            {
                                "Email": 'info@lift9ja.com',
                                "Name": ""
                            }
                        ],
                        "Subject": "New Contact Message",
                        "HTMLPart": message,
                        "CustomID": "AppGettingStartedTest"
                    }
                ]
            }

            mailjet.send.create(data=data)

            messages.success(request, '{} Message submitted. We promise to get back to you as quick as possible.'.format(success))
            return redirect('/contact-us')
        # except:
        #     messages.error(request,
        #                      'An error occurred, please try again later.')
        #     return redirect('/contact-us')


def check_message(request):

    user = MyUser.objects.get(email=request.user)
    # if user.read_mess == False:
    #     return redirect('/messages')

class Welcome(LoginRequiredMixin, View):
    login_url = ulogin

    def get(self, request):

        # if UserType.objects.filter(user=self.request.user).exists():
        #     pass
        # else:
        #     # create User sell price
        #     UserType.objects.create(user=self.request.user)

        ref_link = UserPreference.objects.get(user=request.user)
        testimony = TESTIMONIA.objects.filter(active=True)[:20]

        try:
            read = request.GET['data']
            user = MyUser.objects.get(email=self.request.user.email)
            user.read_message = True
            user.save()
            print(user)
            return redirect('/dashboard')
        except:
            pass

        user = MyUser.objects.get(email=request.user)
        # if user.read_message == False:
        #     return redirect('/messages')

        return render(request,
                      '{}/dash/dashboard.html'.format(appName), {
                      'testimony': testimony,
                      'testimony_count': testimony.count(),
                      'ref_link': ref_link.ref_link
                      })

class PlanSubscription(LoginRequiredMixin, View):
    login_url = ulogin

    def get(self, request):

        user = MyUser.objects.get(email=request.user)
        if user.read_message == False:
            return redirect('/messages')

        Plan = Packages.objects.all()
        data = dict()

        try:
            plan = request.GET['plan']
        except:
            plan = None

        if plan != None:

            print(plan)

            get_plan = Packages.objects.get(id=plan)

            return_price = sum([percentage_calculator(40, get_plan.amount), get_plan.amount])

            print(get_plan)
            data['packages'] = (
                get_plan.daily_earn,
                '{}days'.format(get_plan.contract_period),
                '₦{:,}'.format(return_price),

            )
            return JsonResponse(data, status=200)

        else:

            return render(request, 'investment/subscribe.html',
                          {
                              'plan': Plan
                          })

    def post(self, request):

        get_plan = request.POST['plan']
        customize_gs_withdrawal = request.POST['customize_gs_withdrawal']

        plan = Packages.objects.get(id=get_plan)
        get_user_wallet = UserWallet.objects.get(user=request.user)

        # Create users GS pending plan

        period = int(plan.contract_period)

        if UserGold.objects.filter(user=self.request.user, status='pending', plan=plan).exists():
            gs_mess = 'You are trying to create a replicant GS. You have a pending  {} gold 🪙🪙 worth of {:,},' \
                      ' kindly await for approval or proceed with payment if you have not made payment.'.format(plan.get_plan_display(), plan.amount)
            messages.error(request,
                             '{} {}'.format(success, gs_mess))

            return redirect('/my-gs-data')
        else:
            UserGold.objects.create(user=request.user,
                                    plan=plan,
                                    subscribed_date=current_timezone,
                                    earn_after=customize_gs_withdrawal
                                    )

            gs_mess = 'You have successfully requested to purchase {} gold 🪙🪙 worth of {:,},' \
                      ' kindly proceed with Payments'.format(plan.get_plan_display(), plan.amount)

            notifications('🤝🤝Congratulations {}\n\n'
                          '{}\n\n'
                          'GS will definitely deliver.'
                          .format(get_user_wallet.user.full_name.title(), gs_mess),
                          bot_id, group)

            messages.success(request,
                             '{} Kindly make a payment to the account below to complete your transaction and upload for your GS activation.'.format(success))

        return redirect('/my-gs-data')

class MyOffice(LoginRequiredMixin, View):
    login_url = ulogin

    def get(self, request):
        user = MyUser.objects.get(email=request.user)
        if user.read_message == False:
            return redirect('/messages')

        investments = UserGold.objects.filter(user=self.request.user)

        table = UserGold.objects.filter(user=self.request.user)
        pending = UserGold.objects.filter(user=self.request.user, status='pending')
        active = UserGold.objects.filter(user=self.request.user, status='active')
        ended = UserGold.objects.filter(user=self.request.user, status='ended')

        paginator = Paginator(table, 20)
        page_number = request.GET.get('page')
        get_user_table = paginator.get_page(page_number)

        return render(request, 'investment/investment.html',
                      {
                          'history': get_user_table,
                          'pending': pending.count(),
                          'active': active.count(),
                          'ended': ended.count(),
                      })

# class SellShare(LoginRequiredMixin, View):
#
#     def get(self, request):
#         share_id = request.GET['data']
#         get_user_share_table = Shares.objects.get(user=self.request.user, id=share_id)
#
#         print(get_user_share_table.status)
#
#         if get_user_share_table.status == 'bought':
#             get_user_share_table.status = 'active'
#             get_user_share_table.save()
#
#             messages.success(request,
#                              '{} Your product was successfully placed in the market, you can keep track of your active shares on sales tab.'.format(
#                                  success))
#             return redirect('/my-shares')

@login_required()
def upload_proof(request):

    try:
        if request.method == 'POST':
            file = request.FILES['file']
            gs_id = request.POST['id']

            # check if file exist and return a message
            proof = file.name.replace(' ', '_')

            if UserGold.objects.filter(proof_name=proof).exists():
                messages.error(request, 'Unfortunately, we could not verify this file upload at the moment, please'
                                        ' try again later or contact support.')
                return redirect('/my-gs-data')

            else:
                gs_id = UserGold.objects.get(id=gs_id)
                gs_id.proof = file
                gs_id.state = 'awaiting approval'
                gs_id.proof_name = proof
                gs_id.save()

                messages.success(request, 'Proof uploaded successfully, kindly wait for approval')
                return redirect('/my-gs-data')
    except:
        messages.error(request, 'An error occurred, please only upload jpeg or png files')
        return redirect('/my-gs-dasuccessta')

class MessagesView(LoginRequiredMixin, View):
    def get(self, request):
        mess = AdminMessage.objects.get(user__top_admin=True)
        return render(request, 'dashboard/notifications.html', {
            'mess': mess
        })
