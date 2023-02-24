from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Mentor)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['mentor_name', 'mentor_proffesion']
  search_fields = ['mentor_name', 'mentor_proffesion']

@admin.register(companyClient)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['client_name', 'client_company', 'client_country']
  search_fields = ['client_name', 'client_company', 'client_country']

@admin.register(adsClient)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['ads_client_name', 'ads_client_company', 'ads_client_type_investment']
  search_fields = ['ads_client_name', 'ads_client_company', 'ads_client_type_investment']

admin.site.register(Avatar)