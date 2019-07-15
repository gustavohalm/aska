# Generated by Django 2.2.1 on 2019-07-12 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('number', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('account_number', models.CharField(max_length=56)),
                ('agency', models.CharField(max_length=12)),
                ('number', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('insc_state', models.CharField(max_length=56)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=11)),
                ('born', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('unity', models.CharField(max_length=512)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('cnpj', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='erp.Farm')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=9)),
                ('type', models.CharField(choices=[('Pagar', 'Pagar'), ('Receber', 'Receber')], max_length=12)),
                ('description', models.CharField(max_length=512)),
                ('date', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bill_account', to='erp.Account')),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bank_account', to='erp.BankAccount')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Farm')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.Provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
