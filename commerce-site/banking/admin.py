from django.contrib import admin

from .models import Transactions
from .models import BalanceNotif
from .models import DepositNotif
from .models import WithdrawalNotif
from django.urls import reverse
from django.utils.http import urlencode

# Register your models here.


@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("account_id", "processing_date", "balance", "transaction_type", "amount", "descr")

@admin.register(BalanceNotif)
class BalanceNotifAdmin(admin.ModelAdmin):
    list_display = ("account_id", "is_true", "amount")

@admin.register(DepositNotif)
class BalanceNotifAdmin(admin.ModelAdmin):
    list_display = ("account_id", "is_true")

@admin.register(WithdrawalNotif)
class BalanceNotifAdmin(admin.ModelAdmin):
    list_display = ("account_id", "is_true", "amount")