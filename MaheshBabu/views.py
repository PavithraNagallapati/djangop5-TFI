from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def SuperStar(request):
    return HttpResponse('<h1>SUPER STAR MAHESH BABU NEXT MOVIE WILL BE ON FIRE</H1>')