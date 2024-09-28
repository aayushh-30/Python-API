from django.http import HttpResponse
from django.shortcuts import render

def home(request):
     return HttpResponse("Hello, You are at Home Page")

def about(request):
    return HttpResponse("Hello, You are at About Page")

def contact(request):
    return HttpResponse("Hello, You are at Contact Page")