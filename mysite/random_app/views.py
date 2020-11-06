from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test (request):
    return HttpResponse ("Well, this one looks more like a random app, rather than an index for the polls app, doesn't it?")