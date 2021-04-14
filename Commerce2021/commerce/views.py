from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Transactions, AuthUser
from django.contrib.auth.decorators import login_required
from django.contrib import auth



# Create your views here.

def login(request):
    return render(request, "registration/login.html")

def about(request):
    return render(request, "commerce/about.html")

def contact(request):
    return render(request, "commerce/contact.html")

def hello_there(request, name):
    return render(
        request,
        'commerce/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

@login_required
def transactions(request):
	query_results=Transactions.objects.all() # Collect all records from table 
	return render(request,'commerce/transactions.html',{'query_results':query_results})