from django.shortcuts import render
from django.http import HttpResponse

#Home page
def index(request):
    return  render(request, 'index.html') #HttpResponse("You're at the home page my boy!")

#Art page
def artPage(request):
    return HttpResponse("This is where the art page is gonna go!!!")

#Programming page
def programmingPage(request):
    return HttpResponse("This is where the programming stuff will be!!!")