from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HTTPResponse("<h1> Home Page </h1>")


def room(request):
  return HTTPResponse("<h1> Room </h1>")
    
