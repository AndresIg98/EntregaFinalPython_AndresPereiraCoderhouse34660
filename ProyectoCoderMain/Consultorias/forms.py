from django import forms
from django_countries.fields import CountryField
from datetime import datetime
from django.forms.widgets import SelectDateWidget
from Consultorias.models import *
from django.contrib.admin import widgets
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class MentorForm(forms.Form):

    MENTOR_PROFFESIONS = [
        ("Industrial Engineer", "Industrial Engineer"),
        ("Software Engineer", "Software Engineer"),
        ("Telecommunications Engineer", "Telecommunications Engineer"),
        ("Business Administration and Management", "Business Administration and Management"),
    ]

    range_date_time = datetime.datetime.now().year-16

    mentor_name = forms.CharField(max_length=40)
    mentor_experience_years = forms.IntegerField()
    mentor_date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1940,range_date_time)))
    mentor_proffesion = forms.TypedChoiceField(
        choices=MENTOR_PROFFESIONS, 
        initial="Software Engineer"
    )
    mentor_email = forms.EmailField()

class companyClientForm(forms.Form):
    
    client_name = forms.CharField(max_length=40)
    client_company = forms.CharField(max_length=40)
    client_country = CountryField().formfield()
    client_email = forms.EmailField()
    class Meta:
        unique_together = ["client_company", "client_email"]

class adsClientForm(forms.Form):

    TYPE_INVESTMENT = [
        ("Main Page Logo Mention", "Main Page Logo Mention"),
        ("Sponsored Video", "Sponsored Video"),
        ("Sponsored Post", "Sponsored Post"),
    ]

    ads_client_name = forms.CharField(max_length=40)
    ads_client_company = forms.CharField(max_length=40)
    ads_client_email = forms.EmailField()
    ads_client_investment = forms.IntegerField()
    ads_client_type_investment = forms.TypedChoiceField(
        choices=TYPE_INVESTMENT, 
        initial="Sponsored Post",
    )
    ads_client_date_investment = forms.DateField(widget=forms.SelectDateWidget())

class UserRegister(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class EditForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class AvatarForm(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["image"]