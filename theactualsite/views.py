from django.shortcuts import render
from django.http import HttpResponse
from .models import Art, ArtImg, Programming, ProgImg

#Home page
def index(request):
    return  render(request, 'index.html')

#Art page
def artPage(request):

    #fetch art appropriately
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

    #fetch coding projects
    t_code_list_hobby = ProgImg.objects.filter(associated_piece__type='Hobby').order_by('-associated_piece__year')
    t_code_list_school = ProgImg.objects.filter(associated_piece__type='School').order_by('-associated_piece__year')

    prog_list_h = []
    prog_list_s = []

    for item in t_code_list_hobby:
        if not(itemExists(item, prog_list_h) ):
            prog_list_h.append(item)

    for item in t_code_list_school:
        if not(itemExists(item, prog_list_s) ):
            prog_list_s.append(item)

    context = {
        'prog_list_h': prog_list_h,
        'prog_list_s': prog_list_s,
        'progcount_h': len(prog_list_h),
        'progcount_s': len(prog_list_s),
    }


    return render(request, 'code_portfolio.html', context)


#return the art detail page
def piece_detail(request, artpiece_id):

    artImgObjs = getArtImg(artpiece_id)

    context = {
        'artImgObjs': artImgObjs,
    }

    return render(request, 'art_detail.html', context)


#return the programming detail page
def p_piece_detail(request, progpiece_id):


    progImgObjs = getProgImg(progpiece_id)

    context = {
        'progImgObjs': progImgObjs,
    }

    return render(request, 'prog_detail.html', context)

#gets the art related to the pk passed
#returns in the form of an artImg so i have the art too
#may return multiple in the case there are multiple pics but will be only 1 art
def getArtImg(art_id):
    thePiece = ArtImg.objects.filter(associated_piece=art_id)

    return thePiece

#same as the above but for programming objects instead
def getProgImg(prog_id):
    thePiece = ProgImg.objects.filter(associated_piece=prog_id)

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

#return the robots.txt page for those pesky robits
def robots(request):
    return render(request, 'robots.txt')