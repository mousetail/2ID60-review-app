from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone
from .models import Review, Course, Student, Timeslot
from .forms import RegistrationForm, ReviewForm


def home(request):
    return render(request, "tureview/home.html")


def search(request):
    faculties = Course.FACULTY_OPTIONS
    return render(request, "tureview/search.html", {"faculties": faculties,
                                                    "letters": [(i, i.upper()) for i in 'abcdex'],
                                                    "quartiles": [(i, "Q" + str(i)) for i in range(1, 5)]})


def course(request, code):
    code = code.upper()
    try:
        course = Course.objects.get(id__iexact=code)
    except Course.DoesNotExist:
        return HttpResponse("course \"" + str(code) + "\" does not exist")
    reviews = Review.objects.filter(timeslot__course=course).order_by('date')
    return render(request, "tureview/course.html",
                  {'course': course, 'reviews': reviews})


@login_required
def review(request, code):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_bound and form.is_valid():
            cleaned = form.cleaned_data
            timeslots = Timeslot.objects.filter(
                year=cleaned["year"]).filter(
                letter=cleaned["letter"]).filter(
                quartile=cleaned["quartile"])
            try:
                slot0 = timeslots[0]
            except IndexError:
                form.add_error("letter", "The course "+str(code)+" was not offered in this year, quartile and timeslot")
                slot0 = None

            if slot0:
                assert slot0, repr(slot0)

                student = Student.objects.get(user = request.user)

                review = Review()
                review.date = timezone.now()
                review.reviewLong = cleaned["content"]
                review.reviewShort = cleaned["summary"]
                review.student = student
                review.timeslot = slot0
                review.save()

                return HttpResponseRedirect("..")

    else:
        form = ReviewForm()
    return render(request, "tureview/review.html", {"form": form})


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

# Please don't remove
'''@login_required
def profile(request):
    reviews = Review.objects.filter(student=request.user.student)
    return render(request, "tureview/profile.html", {'reviews': reviews})
'''

def userprofile(request, username):
    user = User.objects.get(username=username) # kan vast eleganter
    student = Student.objects.get(user=user)
    reviews = Review.objects.filter(student=student)
    return render(request, "tureview/profile.html", {'user': user, 'student': student, 'reviews': reviews})
