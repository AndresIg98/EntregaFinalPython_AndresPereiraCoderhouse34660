from django.db import models
import datetime
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.


class Mentor(models.Model):

    MENTOR_PROFFESIONS = [
        ("Industrial Engineer", "Industrial Engineer"),
        ("Software Engineer", "Software Engineer"),
        ("Telecommunications Engineer", "Telecommunications Engineer"),
        ("Business Administration and Management", "Business Administration and Management"),
    ]

    mentor_name = models.CharField(max_length=40)
    mentor_experience_years = models.IntegerField()
    mentor_date_of_birth = models.DateField()
    mentor_proffesion = models.CharField(
        max_length=40,
        choices=MENTOR_PROFFESIONS, 
        default="Software Engineer"
    )
    mentor_email = models.EmailField(unique =True)

    vtoday = datetime.date.today()

    def mentor_age(self): #En algún momento lo usare para insertarlo en el HTML
        vtoday_dateofbirth = self.vtoday-self.mentor_date_of_birth
        final_age = int(round(vtoday_dateofbirth.days/365,0))
        return final_age

class companyClient(models.Model):
    
    client_name = models.CharField(max_length=40)
    client_company = models.CharField(max_length=40)
    client_country = CountryField()
    client_email = models.EmailField()
    class Meta:
        unique_together = ["client_company", "client_email"]

class adsClient(models.Model):

    TYPE_INVESTMENT = [
        ("Main Page Logo Mention", "Main Page Logo Mention"),
        ("Sponsored Video", "Sponsored Video"),
        ("Sponsored Post", "Sponsored Post"),
    ]

    ads_client_name = models.CharField(max_length=40)
    ads_client_company = models.CharField(max_length=40)
    ads_client_email = models.EmailField()
    ads_client_investment = models.IntegerField()
    ads_client_type_investment = models.CharField(
        max_length=40,
        choices=TYPE_INVESTMENT, 
        default="Sponsored Post"
    )
    ads_client_date_investment = models.DateField(default=datetime.date.today)

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to="media", null=True, blank=True)