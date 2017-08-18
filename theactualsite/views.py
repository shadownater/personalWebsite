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
    t_art_list = ArtImg.objects.all().order_by('-associated_piece__year')

    art_list = []
    for item in t_art_list:
        if not(itemExists(item, art_list) ):
            #gets here when item is not in art_list
            art_list.append(item)


    context = {
        'art_list': art_list,
        'artcount': len(art_list),
    }

    return render(request, 'portfolio.html', context)

#Programming page
def programmingPage(request):
    return HttpResponse("This is where the programming stuff will be!!!")

def piece_detail(request, artpiece_id):

    artImgObjs = getArtImg(artpiece_id)
    print artImgObjs
    print artImgObjs[0].id
    print artImgObjs[0].associated_piece.title

    context = {
        'artImgObjs': artImgObjs,
    }

    return render(request, 'art_detail.html', context)


#gets the art related to the pk passed
#returns in the form of an artImg so i have the art too
#may return multiple in the case there are multiple pics but will be only 1 art
def getArtImg(art_id):
    thePiece = ArtImg.objects.filter(associated_piece=art_id)

    return thePiece


#makes sure the art_list only holds 1 copy of the art
#it has to fetch via the artImgs, which can list the art more than once (in the case of a piece having multiple pics)
def itemExists(a, list):
    result = False
    for i in list:
        if a.associated_piece == i.associated_piece:
            result = True
            return result
    return False