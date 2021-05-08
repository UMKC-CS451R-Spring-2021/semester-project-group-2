# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BalanceNotif(models.Model):
    account_id = models.IntegerField(primary_key=True)
    is_true = models.CharField(max_length=1)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balance_notif'


class DepositNotif(models.Model):
    account_id = models.IntegerField(primary_key=True)
    is_true = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'deposit_notif'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    processing_date = models.DateField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    transaction_type = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    descr = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class WithdrawalNotif(models.Model):
    account_id = models.IntegerField(primary_key=True)
    is_true = models.CharField(max_length=1)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'withdrawal_notif'

@receiver(post_save, sender=Transactions, dispatch_uid="check_deposit")
def check_deposit(sender, instance, **kwargs):

    if instance.transaction_type=="CR":
        query_results = DepositNotif.objects.get(account_id = instance.account_id)
        if query_results.is_true == "1":
            print("transaction was a credit")
            send_mail(
                'Credit Update - Commerce Bank',
                'This email is to notify that a Credit has been added to your account.',
                'coykwan@gmail.com',
                ['daylanq10@gmail.com'],
                fail_silently=False,
            )

    if instance.transaction_type=="DR":
        query_results = WithdrawalNotif.objects.get(account_id = instance.account_id)
        if query_results.is_true == "1":
            if instance.amount >= query_results.amount:
                print("transaction was a large withdrawal")
                send_mail(
                    'Withdraw Update - Commerce Bank',
                    'This email is to notify that an amount over your desired amount has been withdrawn from your account.',
                    'coykwan@gmail.com',
                    ['daylanq10@gmail.com'],
                    fail_silently=False,
                )

    query_result = BalanceNotif.objects.get(account_id = instance.account_id)
    print(type(instance.balance))
    print(type(query_result.amount))
    if instance.balance < query_result.amount:
        print("Your account has dropped below your set value")
        send_mail(
            'Balance Update - Commerce Bank',
            'This email is to notify that you that your account has dropped below your desired amount.',
            'coykwan@gmail.com',
            ['daylanq10@gmail.com'],
            fail_silently=False,
        )

