from allauth.socialaccount.models import SocialAccount

from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'index.html')


def Shop_page(request):
    return render(request, 'shop/shop.html')



