from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from banking.models import Transactions  # This shouldnt be needed once database is connected


def hello_there(request, name):
    return render(
        request,
        'commerce/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

<<<<<<< Updated upstream

@login_required
def transactions(request):
    query_results = Transactions.objects.all()  # Collect all records from table
    return render(request, 'commerce/transactions.html', {'query_results': query_results})


=======
>>>>>>> Stashed changes
########

def homepage(request):
    messages.info(request, "Logged out successfully") # Doesnt work will figure out
    return render(request, 'homepage.html')


@login_required
def dashboard(request):
    messages.info(request, "Logged in successfully")
    query_results = Transactions.objects.all()  # Collect all records from table
    # With the database connected we should be able to display the query results where we need to
    return render(request, 'dashboard.html', {'present_logout': True, 'query_results': query_results})


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('/banking/homepage')
