from variables import *

# Create your views here.

class MyReferral(LoginRequiredMixin, View):
    def get(self, request):

        total_ref = UserReferral.objects.filter(user=self.request.user).count()
        active_ref = UserReferral.objects.filter(user=self.request.user, active=True).count()
        not_active = UserReferral.objects.filter(user=self.request.user, active=False).count()

        ref_link = UserPreference.objects.get(user=request.user)

        current_earning = (i.earn for i in UserReferral.objects.filter(
            user=self.request.user,
            active=True,
            withdrawn=False
        ))

        total_earning = (i.earn for i in UserReferral.objects.filter(
            user=self.request.user,
        ))


        ref_earning = sum([i.earn for i in UserReferral.objects.filter(
            user=request.user,
            withdrawn=False,
            active=True
        )])

        return render(request, 'referral/referral.html', {
            'not_active': not_active,
            'active_ref': active_ref,
            'total_ref': total_ref,
            'current_earning': sum(current_earning),
            'total_earning': sum(total_earning),
            'ref_link': ref_link.ref_link,
            'ref_earning': ref_earning,
        })

@login_required
def withdraw_ref(request):

    if UserReferral.objects.filter(user=request.user).exists():

        ref = UserReferral.objects.filter(
            user=request.user,
            withdrawn=False,
            active=True
        )

        ref_earning = ([i.earn for i in ref])

        if sum(ref_earning) >= 1000:

            total_earn = sum(ref_earning)
            user_wallet = UserWallet.objects.get(user=request.user)
            user_wallet.user_balance += total_earn
            user_wallet.save()

            for i in ref:
                # i.active = False
                i.withdrawn = True
                i.withdrawn_date = current_timezone
                i.save()

            mess = '👫 Your referral bonus of ₦{:,} has been added to' \
                   ' your wallet, kindly navigate to your dashboard and click on withdraw.'.format(sum(ref_earning))
            notifications('Referral Bonus Paid\n\n'
                          '🤝🤝 Congratulations {}\n\n'
                          '{}\n\n'
                          '{} Cares '
                          .format(request.user.full_name.title(), mess, site_name),
                          bot_id, group)

            messages.success(request, '₦{:,} successfully added yo your peek wallet balance.'.format(total_earn))
            return redirect('referral:myRef')

        else:
            messages.info(request, 'Minimum of ₦1,000 required to withdraw your referral earning.')
            return redirect('referral:myRef')

    else:
        messages.info(request, 'You have no active referral.')
        return redirect('referral:myRef')
