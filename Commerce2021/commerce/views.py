from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Customer


# Create your views here.

def home(request):
    return render(request, "commerce/home.html")

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

def display(request):
	query_results=Customer.objects.all() # Collect all records from table 
	return render(request,'commerce/display.html',{'query_results':query_results})