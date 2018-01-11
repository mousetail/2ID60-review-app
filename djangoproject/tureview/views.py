from django.shortcuts import render
from django.http import HttpResponse
from .models import Review, Course
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "tureview/home.html")


def search(request):
    faculties = Course.FACULTY_OPTIONS
    return render(request, "tureview/search.html", {"faculties": faculties})


def course(request, code=""):
    #reviews = Review.objects.filter(id__iexact=code).order_by('date')
    reviews = Review.objects.order_by('date')
    return render(request, "tureview/course.html", {'reviews': reviews})


def review(request):
    return render(request, "tureview/review.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
