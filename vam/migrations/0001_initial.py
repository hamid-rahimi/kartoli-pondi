# Generated by Django 5.0 on 2023-12-11 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=7)),
                ('loan_amount', models.FloatField()),
                ('loan_interest', models.FloatField(default=0)),
                ('loan_count_installment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('settling_date', models.DateField()),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vam.loan', verbose_name='کد وام')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member', verbose_name='عضو')),
            ],
        ),
    ]
