# Generated by Django 3.2.1 on 2021-05-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_auto_20210506_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('balance', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommerceUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('f_name', models.CharField(blank=True, max_length=50, null=True)),
                ('l_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'commerce_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('login_password', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('f_name', models.CharField(blank=True, max_length=50, null=True)),
                ('l_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]