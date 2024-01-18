from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from . import templates


def home(request):
    return render(request, 'lgcs/base.html')

def ipc(request):
    return render(request, 'lgcs/ipc.html')

def conveyors(request):
    return render(request, 'lgcs/conveyors.html')