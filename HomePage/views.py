from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def HomePage(request):
    # return HttpResponse('this is homepage.')

def HomePage(request):
    return render(request, 'Main.html')
