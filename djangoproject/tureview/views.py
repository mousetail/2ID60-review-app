from django.shortcuts import render
from django.http import HttpResponse
from .models import Review, Course


def home(request):
    return render(request, "tureview/home.html")


def search(request):
    faculties = Course.FACULTY_OPTIONS
    return render(request, "tureview/search.html", {"faculties": faculties,
                                                    "letters": [(i,i.upper()) for i in 'abcdex'],
                                                    "quartiles": [(i, "Q"+str(i)) for i in range(1,5)]})


def course(request, code=""):
    #reviews = Review.objects.filter(id__iexact=code).order_by('date')
    reviews = Review.objects.order_by('date')
    return render(request, "tureview/course.html", {'reviews': reviews})


def review(request):
    return render(request, "tureview/review.html")


def register(request):
    return HttpResponse("register")
