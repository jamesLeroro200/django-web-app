from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band
from listing.models import Listings

def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {'bands':bands, 'listings':listings})

def apropo(request):
    return render(request, "listings/about.html")

def listings(request):
    listings= Listings.objects.all()
    return render(request, "listings/listings.html", {'listings':listings})
    
def contactus(request):
    return render(request, "listings/contactus.html")