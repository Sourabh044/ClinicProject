from django import views
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.HomePage, name="Dev Clinic"),
    path('Appointments/', views.appointments, name= "Appointments"),
    path('Patients/All', views.patients, name= "Patients"),
    path('Patients/', views.viewpatients, name= "Patients"),
    path('Appointment/<str:pk>/', views.appointment),
    path('Delete-Appointment/<str:pk>/', views.DeleteAppointment),
    path('Add-Appointment/', views.addappointment, name="Add Appointment"),
    # path('Add-Appointment/', views.addappointment, name="Add Appointment"),
    path('Add-Patient/', views.addpatient, name="Add Patient"),
    path('Update-Patient/<str:pk>', views.updatepatient, name="Update Patient"),
    path('SignUp/', views.signup, name="Sign Up"),
    path('Login/', views.Login, name="Sign Up"),
    path('Dashboard/', views.Dashboard, name="Dashboard"),
]