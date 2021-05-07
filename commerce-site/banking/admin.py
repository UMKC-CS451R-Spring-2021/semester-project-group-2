from django.contrib import admin

from .models import Transactions
from django.urls import reverse
from django.utils.http import urlencode

# Register your models here.


@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("account_id", "processing_date", "balance", "transaction_type", "amount", "descr")