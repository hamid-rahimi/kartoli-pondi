# Generated by Django 5.0 on 2023-12-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanpayment',
            name='settling_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]