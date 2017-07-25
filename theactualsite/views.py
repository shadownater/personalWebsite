from django.shortcuts import render
from django.http import HttpResponse
from .models import Art, ArtImg, Programming, ProgImg

#Home page
def index(request):
    return  render(request, 'index.html')

#Art page
def artPage(request):

    #fetch art appropriately
    #probably just go from year and back, not really sure how/if I should categorize this like I have with code stuff
    art_list = ArtImg.objects.all() #Art.objects.all().order_by('year')
    #img_list = ArtImg.objects.all()

    context = {
        'art_list': art_list,
        #'img_list': img_list,
    }

    print(context)

    return render(request, 'portfolio.html', context)

#Programming page
def programmingPage(request):
    return HttpResponse("This is where the programming stuff will be!!!")