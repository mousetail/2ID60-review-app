from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Review, Course, Student
from .forms import RegistrationForm

def home(request):
    return render(request, "tureview/home.html")


def search(request):
    faculties = Course.FACULTY_OPTIONS
    return render(request, "tureview/search.html", {"faculties": faculties,
                                                    "letters": [(i,i.upper()) for i in 'abcdex'],
                                                    "quartiles": [(i, "Q"+str(i)) for i in range(1,5)]})


def course(request, code):
    course = Course.objects.filter(id__iexact=code) # not working yet
    #reviews = Review.objects.filter(id__iexact=code).order_by('date')
    reviews = Review.objects.order_by('date')
    return render(request, "tureview/course.html",
        {'course': course, 'reviews': reviews})

@login_required
def review(request):
    return render(request, "tureview/review.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
    else:
        form = RegistrationForm()
    if form.is_bound and form.is_valid():
        cleaned = form.cleaned_data
        if cleaned['password'] == cleaned['password_2']:
            try:
                existingUser = User.objects.get(username=cleaned["username"])

                form.add_error("username", "username allready taken")
            except User.DoesNotExist:

                user = User.objects.create_user(cleaned["username"], "", cleaned["password"])
                user.save()
                student = Student()
                student.user = user
                student.major = cleaned["major"]
                student.startYear = cleaned["startyear"]
                student.save()

                login(request, user)
                return HttpResponseRedirect("/accounts/profile")
        else:
            form.add_error("password_2", "Passwords do not match")
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    reviews = Review.objects.filter(student=request.user.student)
    return render(request, "tureview/profile.html", {'reviews': reviews})
