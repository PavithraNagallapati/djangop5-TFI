from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def nsn(request):
    return HttpResponse('<h1>Nani was very simple and natural</h1>')