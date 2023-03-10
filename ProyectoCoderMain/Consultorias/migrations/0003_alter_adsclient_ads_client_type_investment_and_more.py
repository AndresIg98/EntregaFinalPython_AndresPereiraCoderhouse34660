# Generated by Django 4.1.5 on 2023-02-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consultorias', '0002_rename_client_companyclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsclient',
            name='ads_client_type_investment',
            field=models.CharField(choices=[('Main Page Logo Mention', 'Main Page Logo Mention'), ('Sponsored Video', 'Sponsored Video'), ('Sponsored Post', 'Sponsored Post')], default='Sponsored Post', max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='mentor_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='companyclient',
            unique_together={('client_company', 'client_email')},
        ),
    ]
