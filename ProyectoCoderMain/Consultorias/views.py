from django.shortcuts import render
from django.db import IntegrityError
from Consultorias.forms import *
from Consultorias.models import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def inicio(request):
    return render(request, "Consultorias/inicio.html")

def about(request):
    return render(request, "Consultorias/about.html")

def pagenoactive(request):
      return HttpResponse(f"Está parte de la página no se encuentra funcionando, próximamente estará disponible.")
 

#Mentores
@login_required
def mentorForm(request):
 
      try:
            if request.method == "POST":
      
                  myMentorForm = MentorForm(request.POST, request.FILES)
                  print(myMentorForm)
      
                  if myMentorForm.is_valid():
                        information = myMentorForm.cleaned_data
                        mentor = Mentor(
                                    mentor_name=information["mentor_name"],
                                    mentor_experience_years=information["mentor_experience_years"],
                                    mentor_date_of_birth=information["mentor_date_of_birth"],
                                    mentor_proffesion=information["mentor_proffesion"],
                                    mentor_email=information["mentor_email"],
                                    )
                        mentor.save()
                  return render(request, "Consultorias/inicio.html")
            else:
                  myMentorForm = MentorForm()
            return render(request, "Consultorias/mentors/mentorForm.html", {"myMentorForm": myMentorForm})
      except IntegrityError as e:
           return HttpResponse(f"El correo {mentor.mentor_email} ya existe, intentalo de nuevo.")
        
def mentorsearchresults(request):

      if request.method == "GET":

            mymentorsearchname = request.GET["mentor_name"]
            mentorsobjectsresults = Mentor.objects.filter(mentor_name__icontains=mymentorsearchname)
            return render(request,"Consultorias/mentors/resultsearchmentors.html", {"mentor_name":mymentorsearchname, "resultados":mentorsobjectsresults})


      return render(request, "Consultorias/mentors/resultsearchmentors.html")

@login_required      
def updatementor(request, mentorName):

      mentor = Mentor.objects.get(mentor_name = mentorName)

      try:
            if request.method == "POST":
      
                  myMentorForm = MentorForm(request.POST)
                  print(myMentorForm)
      
                  if myMentorForm.is_valid():

                        information = myMentorForm.cleaned_data

                        mentor.mentor_name = information["mentor_name"]
                        mentor.mentor_experience_years = information["mentor_experience_years"]
                        mentor.mentor_date_of_birth = information["mentor_date_of_birth"]
                        mentor.mentor_proffesion = information["mentor_proffesion"]
                        mentor.mentor_email = information["mentor_email"]

                        mentor.save()

                  return render(request, "Consultorias/inicio.html")
            else:
                  myMentorForm = MentorForm(initial={"mentor_name":mentor.mentor_name,"mentor_experience_years":mentor.mentor_experience_years,
                                                     "mentor_date_of_birth":mentor.mentor_date_of_birth,"mentor_proffesion":mentor.mentor_proffesion,
                                                     "mentor_email":mentor.mentor_email})
            return render(request, "Consultorias/mentors/mentorEditForm.html", {"myMentorForm": myMentorForm, "name":mentorName})
      except IntegrityError as e:
           return HttpResponse(f"El correo {mentor.mentor_email} ya existe, intentalo de nuevo.")
            

class mentordelete(LoginRequiredMixin, DeleteView):

      model = Mentor
      success_url = "/Consultorias/mentor/list"
      template_name = "Consultorias/mentors/mentor_confirm_delete.html"


class mentorList(LoginRequiredMixin, ListView):

      model = Mentor
      template_name= "Consultorias/mentors/mentor_list.html"

class mentorDetail(LoginRequiredMixin, DetailView):

      model = Mentor
      template_name= "Consultorias/mentors/mentor_detail.html"
      

#Company Clients
@login_required
def companyclientForm(request):
 
      try:
            if request.method == "POST":
      
                  myCompanyClientForm = companyClientForm(request.POST)
                  print(myCompanyClientForm)
      
                  if myCompanyClientForm.is_valid():
                        information = myCompanyClientForm.cleaned_data
                        mycompanyclient = companyClient(
                                    client_name=information["client_name"],
                                    client_company=information["client_company"],
                                    client_country=information["client_country"],
                                    client_email=information["client_email"],
                                    )
                        mycompanyclient.save()
                  return render(request, "Consultorias/inicio.html")
            else:
                  myCompanyClientForm = companyClientForm()
            return render(request, "Consultorias/companyclients/companyclientForm.html", {"myCompanyClientForm": myCompanyClientForm})
      except IntegrityError as e:
           return HttpResponse(f"El correo {mycompanyclient.client_email} y la compañia {mycompanyclient.client_company} ya existe, intentalo de nuevo.")

@login_required
def updatecompanyclient(request, companyclientName):

      companyclient = companyClient.objects.get(client_name = companyclientName)

      try:
            if request.method == "POST":
      
                  myCompanyClientForm = companyClientForm(request.POST)
                  print(myCompanyClientForm)
      
                  if myCompanyClientForm.is_valid():
                        information = myCompanyClientForm.cleaned_data
                        
                        companyclient.client_name=information["client_name"]
                        companyclient.client_company=information["client_company"]
                        companyclient.client_country=information["client_country"]
                        companyclient.client_email=information["client_email"]
                                    
                        companyclient.save()
                  return render(request, "Consultorias/inicio.html")
            else:
                  myCompanyClientForm = companyClientForm(initial={"client_name":companyclient.client_name,
                                                                   "client_company":companyclient.client_company,
                                                                   "client_country":companyclient.client_country,
                                                                   "client_email":companyclient.client_email})
            return render(request, "Consultorias/companyclients/companyclientEditForm.html", {"myCompanyClientForm": myCompanyClientForm,"name":companyclientName})
      except IntegrityError as e:
           return HttpResponse(f"El correo {companyclient.client_email} y la compañia {companyclient.client_company} ya existe, intentalo de nuevo.")

class companyclientList(LoginRequiredMixin,ListView):

      model = companyClient
      template_name= "Consultorias/companyclients/companyclient_list.html"

class companyclientDetail(LoginRequiredMixin,DetailView):

      model = companyClient
      template_name= "Consultorias/companyclients/companyclient_detail.html"

class companyclientdelete(LoginRequiredMixin,DeleteView):

      model = companyClient
      success_url = "/Consultorias/companyclient/list"
      template_name = "Consultorias/companyclients/companyclient_confirm_delete.html"


#ads company clients

@login_required
def adsclientForm(request):
 
      if request.method == "POST":

            myadsClientForm = adsClientForm(request.POST)
            print(myadsClientForm)

            if myadsClientForm.is_valid():
                  information = myadsClientForm.cleaned_data
                  myadsclient = adsClient(
                              ads_client_name=information["ads_client_name"],
                              ads_client_company=information["ads_client_company"],
                              ads_client_email=information["ads_client_email"],
                              ads_client_investment = information["ads_client_investment"],
                              ads_client_type_investment = information["ads_client_type_investment"],
                              ads_client_date_investment = information["ads_client_date_investment"]
                              )
                  myadsclient.save()
            return render(request, "Consultorias/inicio.html")
      else:
            myadsClientForm = adsClientForm()
      return render(request, "Consultorias/adsclients/adsclientform.html", {"myadsClientForm": myadsClientForm})
      
@login_required
def adsclientupdate(request, adsclientName):

      adsclient = adsClient.objects.get(ads_client_name = adsclientName)

      if request.method == "POST":

            myadsClientForm = adsClientForm(request.POST)
            print(myadsClientForm)

            if myadsClientForm.is_valid():

                  information = myadsClientForm.cleaned_data
                  adsclient.ads_client_name = information["ads_client_name"]
                  adsclient.ads_client_company = information["ads_client_company"]
                  adsclient.ads_client_email = information["ads_client_email"]
                  adsclient.ads_client_investment = information["ads_client_investment"]
                  adsclient.ads_client_type_investment = information["ads_client_type_investment"]
                  adsclient.ads_client_date_investment = information["ads_client_date_investment"]
                  adsclient.save()

            return render(request, "Consultorias/inicio.html")
      else:
            myadsClientForm = adsClientForm(initial={"ads_client_name":adsclient.ads_client_name,
                                                     "ads_client_company":adsclient.ads_client_company,
                                                     "ads_client_email":adsclient.ads_client_email,
                                                     "ads_client_investment":adsclient.ads_client_investment,
                                                     "ads_client_type_investment":adsclient.ads_client_type_investment,
                                                     "ads_client_date_investment":adsclient.ads_client_date_investment})
      return render(request, "Consultorias/adsclients/adsclientEditForm.html", {"myadsClientForm": myadsClientForm, "name":adsclientName})

class adsclientList(LoginRequiredMixin,ListView):

      model = adsClient
      template_name= "Consultorias/adsclients/adsclient_list.html"

class adsclientDetail(LoginRequiredMixin,DetailView):

      model = adsClient
      template_name= "Consultorias/adsclients/adsclient_detail.html"

class adsclientdelete(LoginRequiredMixin,DeleteView):

      model = adsClient
      success_url = "/Consultorias/adsclient/list"
      template_name = "Consultorias/adsclients/adsclient_confirm_delete.html"

#login request

def login_request(request):

      if request.method == "POST":

            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():

                  usuario = form.cleaned_data.get("username")
                  contraseña = form.cleaned_data.get("password")


                  user = authenticate(username = usuario, password = contraseña)

                  if user:
                        login(request, user)

                        return render(request, "Consultorias/inicio.html", {"mensaje":f"Iniciaste sesión correctamente {user}"})
                  
            else:
                  return render(request, "Consultorias/inicio.html", {"mensaje":"Credenciales invalidas."})
      else:

            form = AuthenticationForm()
      
      return render(request, "Consultorias/login.html", {"form":form})

def signup(request):

      if request.method == "POST":
      
            form = UserRegister(request.POST)

            if form.is_valid():
                  
                  username = form.cleaned_data["username"]
                  form.save()

                  return render(request, "Consultorias/inicio.html", {"mensaje":"Usuario creado"})
      
      else:
            form = UserRegister()
      
      return render(request, "Consultorias/registro.html", {"form":form})

@login_required
def edituser(request):

      user = request.user

      if request.method == "POST":

            form = EditForm(request.POST)

            if form.is_valid():

                  info = form.cleaned_data

                  user.email = info["email"]
                  user.set_password(info["password1"])
                  user.first_name = info["first_name"]
                  user.last_name = info["last_name"]

                  user.save()

                  update_session_auth_hash(request, user)

                  return render(request, "Consultorias/inicio.html")
      
      else:
            form = EditForm(initial = {"email":user.email,
                                       "first_name":user.first_name,
                                       "last_name":user.last_name})
      
      return render(request, "Consultorias/editprofile.html", {"form":form,"user":user})

#avatar
@login_required
def addAvatar(request):

      if request.method=="POST":

            form = AvatarForm(request.POST, request.FILES)

            if form.is_valid():

                  actualUser = User.objects.get(username=request.user)

                  avatar = Avatar(user=actualUser, image=form.cleaned_data["image"])

                  avatar.save()

                  return render(request, "Consultorias/inicio.html")
      
      else:
            form = AvatarForm()

      return render(request, "Consultorias/addavatar.html",{"form":form})