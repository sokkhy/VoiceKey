from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse("hello this is my djando app")
# Create your views here.
