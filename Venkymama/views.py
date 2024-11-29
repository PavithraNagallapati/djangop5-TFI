from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dvm(request):
    return HttpResponse('<h1>VENKY MAMA WAS VERY ENERGETIC</h1>')