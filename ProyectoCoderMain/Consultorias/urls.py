from django.urls import path
from Consultorias import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),

    path('aboutme/', views.about, name="aboutme"),

    path('noactive/', views.pagenoactive, name="noactive"),

    #CRUD Mentores
    path('crear_mentor/', views.mentorForm, name="crear_mentor"),
    path('mentor/list',views.mentorList.as_view(), name = "resultados_mentores"),
    path('mentor/<int:pk>',views.mentorDetail.as_view(), name = "detalle_mentor"),
    path('buscaresult_mentores/',views.mentorsearchresults, name = "buscaresult_mentores"),
    path('mentor/eliminar/<int:pk>',views.mentordelete.as_view(), name = "borrar_mentores"),
    path('editar_mentores/<mentorName>/',views.updatementor, name = "editar_mentores"),

    #CRUD Company Clients
    path('crear_company_client/', views.companyclientForm, name = "crear_company_client"),
    path('companyclient/list',views.companyclientList.as_view(), name = "resultados_company_client"),
    path('companyclient/<int:pk>',views.companyclientDetail.as_view(), name = "detalle_company_client"),
    path('companyclient/eliminar/<int:pk>',views.companyclientdelete.as_view(), name = "borrar_company_client"),
    path('editar_companyclient/<companyclientName>/',views.updatecompanyclient, name = "editar_company_client"),

    #CRUD ads clients
    path('crear_patrocinador/',views.adsclientForm, name = "crear_patrocinador"),
    path('adsclient/list',views.adsclientList.as_view(), name = "resultados_patro"),
    path('adsclient/<int:pk>',views.adsclientDetail.as_view(), name = "detalle_patro"),
    path('adsclient/eliminar/<int:pk>',views.adsclientdelete.as_view(), name = "eliminar_patro"),
    path('editar_patrocinadores/<adsclientName>/',views.adsclientupdate, name = "editar_patro"),


    #login
    path('login/', views.login_request, name="inicio_sesion"),
    path('signup/', views.signup, name="registro"),
    path('logout/', LogoutView.as_view(template_name="Consultorias/logout.html"), name="cerrar_sesion"),

    #Edit profiles
    path('editar_usuario/', views.edituser, name="editar_usuario"),
    path('agregar_avatar/', views.addAvatar, name="agregar_avatar"),
]