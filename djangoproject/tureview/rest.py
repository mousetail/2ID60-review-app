import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models

@csrf_exempt
def search(request):
    # code, facultijd, jaar, quartiel, tijdslot
    code = request.POST.get("code", "")
    facultijd = request.POST.get("fac", "")
    cname = request.POST.get("name", "")
    year = request.POST.get("year", "0")
    quartile = request.POST.get("quartile", "-1")
    if quartile != "":
        quartile = int(quartile)
    else:
        quartile=-1
    if year != "":
        year = int(year)
    else:
        year = 0
    timeslot = request.POST.get("slot", "")

    error = ""
    results = ["2ID60"]
    if code != "":
        try:
            results = [models.Course.objects.get(id=code)]
        except models.Course.DoesNotExist:
            error = "no course with code \"" + code + "\" found"

    else:
        courses = models.Course.objects.all()
        if facultijd != "":
            courses = courses.filter(faculty=facultijd)
        if cname != "":
            courses = courses.filter(name__icontains=cname)
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
                    slots[result.year] = {results.quartile: [result.letter]}
            else:
                output[result.course.id] = {"id": result.course.id, "shortDesc": result.course.descriptionShort,
                       "longDest": result.course.descriptionLong,
                        "name": result.course.name, "years": {result.year: {result.quartile: [result.letter]}}}
        output = list(output.values())
        output.sort(key=lambda x: x["id"])

    return HttpResponse(json.dumps(output), content_type="application/json")
