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
    t_art_list = ArtImg.objects.all()

    art_list = []
    for item in t_art_list:
        if not(itemExists(item, art_list) ):
            #gets here when item is not in art_list
            art_list.append(item)


    context = {
        'art_list': art_list,
    }

    print(context)

    return render(request, 'portfolio.html', context)

#Programming page
def programmingPage(request):
    return HttpResponse("This is where the programming stuff will be!!!")


def itemExists(a, list):
    result = False
    for i in list:
        if a.associated_piece == i.associated_piece:
            result = True
            return result
    return False