from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You're at the home page my boy!")

def artPage(request):
    return HttpResponse("This is where the art page is gonna go!!!")

def programmingPage(request):
    return HttpResponse("This is where the programming stuff will be!!!")