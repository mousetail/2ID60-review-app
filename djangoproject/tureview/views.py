from django.shortcuts import render
from django.http import HttpResponse
from .models import Review


def home(request):
    return render(request, "tureview/home.html")


def search(request):
    return render(request, "tureview/search.html", {"abc": "def"})


def course(request, code=""):
    #reviews = Review.objects.filter(id__iexact=code).order_by('date')
    reviews = Review.objects.order_by('date')
    return render(request, "tureview/course.html", {'reviews': reviews})


def review(request):
    return render(request, "tureview/review.html")


def register(request):
    return HttpResponse("register")
