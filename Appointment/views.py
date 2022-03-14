from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def Appointment(request):
#     return HttpResponse("Appintment page setup success.")

def Appointment(request):
    return render(request, 'Appointment.html')
