from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def my_view(request):
    return HttpResponse("Hello, world!")