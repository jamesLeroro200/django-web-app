from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Band
from listing.models import Listings

def hello(request):
    bands = Band.objects.all()
    listings= Listings.objects.all()
    return HttpResponse(f"""
    <h1>Bienvenu sur mon app Django</h1>
    <p>Mes meilleurs groupes sont :</p>
        <ul>
            <li>{bands[0].name} <p>{listings[0].titre}</p></li>
            <li>{bands[1].name} <p>{listings[1].titre}</p></li>
            <li>{bands[2].name} <p>{listings[2].titre}</p></li>
        <ul/>
    """)

def apropo(request):
    return HttpResponse("<h1>A propos </h1> <p>Nous adorons merch</p>")

def listings(request):
    return HttpResponse('/listing/views.py')
def contactus(request):
    return HttpResponse('/listing/contactus.py')