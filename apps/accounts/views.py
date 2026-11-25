from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import CivilianAccount, OfficialAccount, ModeratorAccount
from ..donation.models import Donation
from ..donation_drive.models import DonationDrive
# Create your views here.
@login_required
def accounts(request):
    user = request.user
    civilian_account = CivilianAccount.objects.filter(user=user).first()
    official_account = OfficialAccount.objects.filter(user=user).first()
    moderator_account = ModeratorAccount.objects.filter(user=user).first()
    return render(request, "accounts/accounts.html", {"civilian_account":civilian_account, "official_account": official_account, "moderator_account": moderator_account})

@login_required
def official_account(request):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    if official_account is None:
        return redirect("home:home")
    return render(request, "accounts/official_account.html", { "official_account": official_account})

@login_required
def civilian_account(request):
    civilian_account = CivilianAccount.objects.get(user=request.user)
    donations = Donation.objects.filter(civilian_account=civilian_account).select_related('donation_drive')
    return render(request, "accounts/civilian_account.html", { "civilian_account": civilian_account, "donations":donations})