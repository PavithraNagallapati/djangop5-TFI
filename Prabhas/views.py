from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rspr(request):
    return HttpResponse('<h1>Prabhas is the pan india star</h1')