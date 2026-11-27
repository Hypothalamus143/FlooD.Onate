from django.shortcuts import render, redirect
from ..verification_request.models import VerificationRequest
from ..accounts.models import ModeratorAccount, OfficialAccount
from ..users.models import User
from ..accounts.forms import OfficialAccountForm
from ..verification_request.forms import VerificationRequestManagementForm
from ..profiles.models import Profile
from django.db.models import Subquery

# Create your views here.
def moderator(request):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    return render(request, "moderator/moderator.html")

def verification_requests(request):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    verification_requests = VerificationRequest.objects.all()
    status = request.GET.get("status")
    if(status):
        verification_requests = verification_requests.filter(status=status)
    verification_requests = verification_requests.select_related('user')
    return render(request, "moderator/verification_requests.html", {"verification_requests":verification_requests})

def verification_details(request, id):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    verification_request = VerificationRequest.objects.get(id=id)
    official_account = OfficialAccount.objects.get(user=user)
    user = verification_request.user
    profile = Profile.objects.get(user=user)
    official_account = OfficialAccount.objects.get(user=user)
    if request.method == "POST":
        form_official_account = OfficialAccountForm(request.POST, instance=official_account)
        form_verification_request = VerificationRequestManagementForm(request.POST, instance=verification_request)
        if form_official_account.is_valid():
            official_account = form_official_account.save(commit=False)
            official_account.user = user
            official_account.save()
            verification_request.status=3
            return redirect("moderator:verification_requests")
        elif form_verification_request.is_valid():
            form_verification_request.save()
            return redirect("moderator:verification_requests")
        print("Not Valid")
    form_official_account = OfficialAccountForm(instance=official_account)
    form_verification_request = VerificationRequestManagementForm(instance=verification_request)
    return render(request, "moderator/verification_details.html", {"verification_request":verification_request, "user":user, "form_official_account":form_official_account, "form_verification_request":form_verification_request, "profile":profile})

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