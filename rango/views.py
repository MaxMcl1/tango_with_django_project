from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey visit about <br/> <a href='/rango/about/'>About</a>")

def about(requesty):
    return HttpResponse("Maxo says this is about <a href='/rango/'>Index</a>")

