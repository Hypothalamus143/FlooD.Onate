from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import CivilianAccount, OfficialAccount, ModeratorAccount
from ..donation.models import Donation
from ..profiles.models import Profile
from django.utils import timezone
# Create your views here.
@login_required
def accounts(request):
    user = request.user
    civilian_account = CivilianAccount.objects.filter(user=user).first()
    official_account = OfficialAccount.objects.filter(user=user).first()
    moderator_account = ModeratorAccount.objects.filter(user=user).first()
    return render(request, "accounts/accounts.html", {"civilian_account":civilian_account, "official_account": official_account, "moderator_account": moderator_account})

@login_required
def official_account(request, id):
    official_account_user = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    official_account_query = OfficialAccount.objects.get(id=id)
    user = official_account_query.user
    profile = Profile.objects.get(user=user)
    
    return render(request, "accounts/official_account.html", { "official_account_user": official_account_user, "official_account_query":official_account_query, "profile":profile, "user":user})

@login_required
def civilian_account(request):
    civilian_account = CivilianAccount.objects.get(user=request.user)
    donations = Donation.objects.filter(civilian_account=civilian_account).select_related('donation_drive')
    return render(request, "accounts/civilian_account.html", { "civilian_account": civilian_account, "donations":donations})