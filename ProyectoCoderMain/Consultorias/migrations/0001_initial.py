# Generated by Django 4.1.5 on 2023-02-02 22:22

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adsClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads_client_name', models.CharField(max_length=40)),
                ('ads_client_company', models.CharField(max_length=40)),
                ('ads_client_email', models.EmailField(max_length=254)),
                ('ads_client_investment', models.IntegerField()),
                ('ads_client_type_investment', models.CharField(choices=[('Main Page Logo Mention', 'Main Page Logo Mention'), ('Sponsored Video', 'Sponsored Video'), ('Sponsored Post', 'Sponsored Post')], default='Sponsored Post', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=40)),
                ('client_company', models.CharField(max_length=40)),
                ('client_country', django_countries.fields.CountryField(max_length=2)),
                ('client_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_name', models.CharField(max_length=40)),
                ('mentor_experience_years', models.IntegerField()),
                ('mentor_date_of_birth', models.DateField()),
                ('mentor_proffesion', models.CharField(choices=[('Industrial Engineer', 'Industrial Engineer'), ('Software Engineer', 'Software Engineer'), ('Telecommunications Engineer', 'Telecommunications Engineer'), ('Business Administration and Management', 'Business Administration and Management')], default='Software Engineer', max_length=40)),
                ('mentor_email', models.EmailField(max_length=254)),
            ],
        ),
    ]