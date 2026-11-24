from django.shortcuts import render, redirect
from ..verification_request.models import VerificationRequest
from ..accounts.models import ModeratorAccount, OfficialAccount
from ..users.models import User
from ..accounts.forms import OfficialAccountForm
from django.db.models import Subquery

# Create your views here.
def moderator(request):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    return render(request, "moderator/moderator.html")

def verification_requests(request):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    verification_requests = VerificationRequest.objects.select_related('user')
    return render(request, "moderator/verification_requests.html", {"verification_requests":verification_requests})

def verification_details(request, id):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    user = User.objects.get(id=id)
    verification_request = VerificationRequest.objects.get(user=user)
    if request.method == "POST":
        form = OfficialAccountForm(request.POST)
        if form.is_valid():
            official_account = form.save(commit=False)
            official_account.user = user
            official_account.save()
            verification_request.delete()
            return redirect("moderator:verification_requests")
    form = OfficialAccountForm()
    return render(request, "moderator/verification_details.html", {"verification_request":verification_request, "user":user, "form":form})

def moderators(request):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    moderators = ModeratorAccount.objects.select_related('user')
    return render(request, "moderator/moderators.html", {"moderators":moderators})

def non_moderators(request):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    user_ids = ModeratorAccount.objects.values('user_id')
    non_moderators = User.objects.exclude(
        id__in = Subquery(user_ids)
    ).filter(is_superuser=False)
    return render(request, "moderator/non_moderators.html", {"non_moderators":non_moderators})