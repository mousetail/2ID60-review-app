import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
from .models import Student, Review

@csrf_exempt
def search(request):
    # code, facultijd, jaar, quartiel, tijdslot
    code = request.POST.get("code", "")
    faculty = request.POST.get("fac", "")
    cname = request.POST.get("name", "")
    year = request.POST.get("year", "0")
    quartile = request.POST.get("quartile", "-1")
    minRating = request.POST.get("minRating", "0")

    sortfunc = request.POST.get("sort", "id")

    if quartile != "":
        quartile = int(quartile)
    else:
        quartile=-1
    if year != "":
        year = int(year)
    else:
        year = 0
    if minRating != "":
        minRating = float(minRating)
    else:
        minRating = 0
    timeslot = request.POST.get("slot", "")

    error = ""
    results = []
    if code != "":
        try:
            results = [models.Course.objects.get(id=code)]
        except models.Course.DoesNotExist:
            error = "no course with code \"" + code + "\" found"

    else:
        courses = models.Course.objects.all()
        if faculty != "":
            courses = courses.filter(faculty=faculty)
        if cname != "":
            courses = courses.filter(name__icontains=cname)
        if minRating > 0:
            courses = courses.filter(averageRating__gte=minRating)
        timeslots = models.Timeslot.objects.all()
        timeslots = timeslots.filter(course__in=courses)
        if year != 0:
            timeslots = timeslots.filter(year=year)

        if timeslot != "":
            timeslots = timeslots.filter(letter__iexact=timeslot[0].lower())

        if quartile != -1:
            timeslots = timeslots.filter(quartile=quartile)


        results = timeslots
    if error:
        output = {"error": error}
    else:
        output = {}
        for result in results:
            if result.course.id in output:
                slots = output[result.course.id]["years"]
                if result.year in slots:
                    quartile = slots[result.year]
                    if result.quartile in quartile:
                        quartile[result.quartile].append(result.letter)
                    else:
                        quartile[result.quartile] = [result.letter]
                else:
                    slots[result.year] = {result.quartile: [result.letter]}
            else:
                output[result.course.id] = {"id": result.course.id, "shortDesc": result.course.descriptionShort,
                       "longDest": result.course.descriptionLong, "avgRating": result.course.getAverage(),
                        "numReviews": result.course.reviewNumber,
                        "name": result.course.name, "years": {result.year: {result.quartile: [result.letter]}}}
        output = list(output.values())
        sortfuncs = {"id": lambda x: x["id"],
                     "name": lambda x: x["name"],
                     "rating": lambda x: 10 - float(x["avgRating"]),
                     "number": lambda x: -x["numReviews"]}
        output.sort(key=sortfuncs[sortfunc])


    return HttpResponse(json.dumps(output), content_type="application/json")

@csrf_exempt
def thumbs(request, code):
    if request.method == 'POST':
        student = Student.objects.get(user=request.user)
        upDown = request.POST.get("thumbs", "")
        review_pk = request.POST.get("review_pk", "")
        review = Review.objects.get(pk=review_pk)
        rtn = 'none'
        if upDown == 'up': # student clicked 'up'
            if Review.objects.filter(pk=review.pk, thumbsDown__pk=student.pk).exists():
                review.thumbsDown.remove(student)
                review.thumbsUp.add(student)
                rtn = 'up'
            elif Review.objects.filter(pk=review.pk, thumbsUp__pk=student.pk).exists():
                review.thumbsUp.remove(student)
                rtn = 'none'
            else:
                review.thumbsUp.add(student)
                rtn = 'up'
        elif upDown == 'down': # student clicked 'down'
            if Review.objects.filter(pk=review.pk, thumbsUp__pk=student.pk).exists():
                review.thumbsUp.remove(student)
                review.thumbsDown.add(student)
                rtn = 'down'
            elif Review.objects.filter(pk=review.pk, thumbsDown__pk=student.pk).exists():
                review.thumbsDown.remove(student)
                rtn = 'none'
            else:
                review.thumbsDown.add(student)
                rtn = 'down'
        return HttpResponse(json.dumps({"state": rtn}), content_type="application/json")
