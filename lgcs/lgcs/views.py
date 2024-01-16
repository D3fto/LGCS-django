from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from . import templates


def home(request):
    return render(request, 'base.html')