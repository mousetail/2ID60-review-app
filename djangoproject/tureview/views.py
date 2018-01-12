from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone
from .models import Review, Course, Student, Timeslot
from .forms import RegistrationForm, ReviewForm


def home(request):
    topcourses = Course.objects.all().order_by('averageRating')[:3]
    return render(request, "tureview/home.html", {'topcourses': topcourses})


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

    slots = Timeslot.objects.filter(course__id__iexact=code)
    gys = [(i.quartile, i.letter) for i in slots]
    gys = set(gys)
    gys2 = [(str(i[0])+","+str(i[1]), "Q"+str(i[0])+" timeslot "+str(i[1])) for i in gys]

    if request.method == "POST":
        form = ReviewForm(gys2, request.POST)
        if form.is_bound and form.is_valid():
            cleaned = form.cleaned_data
            timeslots = Timeslot.objects.filter(
                course__id__iexact=code).filter(
                year=cleaned["year"]).filter(
                letter=cleaned["timeslot"][1]).filter(
                quartile=cleaned["timeslot"][0])
            try:
                slot0 = timeslots[0]
            except IndexError:
                form.add_error("timeslot", "The course "+str(code)+" was not offered in this year, quartile and timeslot")
                slot0 = None

            if slot0:
                assert slot0, repr(slot0)

                student = Student.objects.get(user=request.user)

                review = Review()
                review.date = timezone.now()
                review.reviewLong = cleaned["content"]
                review.reviewShort = cleaned["summary"]
                review.student = student
                review.timeslot = slot0
                review.ratingOverall = cleaned["rating"]
                review.save()

                try:
                    course = Course.objects.get(id__iexact=code)
                except Course.DoesNotExist:
                    return HttpResponse("unexpeted database error (course appears to be deleted")

                average = Review.objects.filter(timeslot__course = course).aggregate(
                    Avg('ratingOverall'), Count('ratingOverall'))
                course.averageRating = average["ratingOverall__avg"]
                course.reviewNumber = average["ratingOverall__count"]
                course.save()

                return HttpResponseRedirect("..")

    else:
        form = ReviewForm(gys2)
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
@login_required
def profile(request):
    user = request.user
    student = Student.objects.get(user=user)
    reviews = Review.objects.filter(student=request.user.student)
    return render(request, "tureview/profile.html", {'user': user, 'student': student, 'reviews': reviews})

def userprofile(request, username):
    user = User.objects.get(username=username) # kan vast eleganter
    student = Student.objects.get(user=user)
    reviews = Review.objects.filter(student=student)
    return render(request, "tureview/profile.html", {'user': user, 'student': student, 'reviews': reviews})
