# Generated by Django 4.1.5 on 2023-02-04 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consultorias', '0003_alter_adsclient_ads_client_type_investment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adsclient',
            name='ads_client_date_investment',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
