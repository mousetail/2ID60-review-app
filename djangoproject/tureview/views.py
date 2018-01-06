from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("home")


def search(request):
    return render(request, "tureview/search.html", {"abc": "def"})


def course(request, code=""):
    return HttpResponse("course")


def review(request):
    return HttpResponse("request")


def register(request):
    return HttpResponse("register")
