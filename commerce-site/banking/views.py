from datetime import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import *

from banking.models import Transactions  # This shouldnt be needed once database is connected


def homepage(request):
    # messages.info(request, "Logged out successfully")  # Doesnt work will figure out
    return render(request, 'homepage.html')


@login_required
def dashboard(request):
    # messages.info(request, "Logged in successfully")
    current_user = request.user.username

    if request.GET.get('mybtn'):
        query_results = Transactions.objects.filter(account_id=current_user) & Transactions.objects.filter(
            transaction_type="CR")

    elif request.GET.get('mybtn_2'):
        query_results = Transactions.objects.filter(account_id=current_user) & Transactions.objects.filter(
            transaction_type="DR")

    elif request.GET.get('mybtn_3'):
        query_results = Transactions.objects.filter(account_id=current_user) & Transactions.objects.filter(
            amount__gt=100)

    elif request.GET.get('normal_btn'):
        query_results = Transactions.objects.filter(account_id=current_user)

    else:
        query_results = Transactions.objects.filter(account_id=current_user)

    # With the database connected we should be able to display the query results where we need to
    return render(request, 'dashboard.html', {'present_logout': True, 'query_results': query_results})


def notifications(request):
    user = request.user.username
    data = DepositNotif.objects.get(account_id=user)
    if request.POST.get('check_1'):
        data.is_true = 1
        data.save()
        return render(request, 'notifications.html')

    if request.POST.get('delete_1'):
        data.is_true = 0
        data.save()
        return render(request, 'notifications.html')

    data = BalanceNotif.objects.get(account_id=user)
    if request.POST.get('check_2'):
        data.is_true = 1
        data.amount = request.POST.get('number_1')
        data.save()
        return render(request, 'notifications.html')

    if request.POST.get('delete_2'):
        data.is_true = 0
        data.save()
        return render(request, 'notifications.html')

    data = WithdrawalNotif.objects.get(account_id=user)
    if request.POST.get('check_3'):
        data.is_true = 1
        data.amount = request.POST.get('number_2')
        data.save()
        return render(request, 'notifications.html')

    if request.POST.get('delete_3'):
        data.is_true = 0
        data.save()
        return render(request, 'notifications.html')

    return render(request, 'notifications.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('/banking/homepage')
