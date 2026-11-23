from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..accounts.models import CivilianAccount, OfficialAccount, ModeratorAccount
# Create your views here.
@login_required
def accounts(request):
    user = request.user
    civilian_account = CivilianAccount.objects.filter(user=user).first()
    official_account = OfficialAccount.objects.filter(user=user).first()
    moderator_account = ModeratorAccount.objects.filter(user=user).first()
    return render(request, "accounts/accounts.html", {"civilian_account":civilian_account, "official_account": official_account, "moderator_account": moderator_account})