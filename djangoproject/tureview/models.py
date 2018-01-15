from django.db import models
from django.utils import timezone


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=199)
    descriptionShort = models.CharField(max_length=200)
    descriptionLong = models.TextField()
    averageRating = models.FloatField(default=0)
    reviewNumber = models.IntegerField(default=0)

    FACULTY_OPTIONS = (
        ('BMT', 'Biomedishe Technologie'),
        ('BK', 'Bouwkunde'),
        ('ESoE', 'Eindhoven School of Education'),
        ('EE', 'Electrical Engineering'),
        ('ID', 'Industrial Design'),
        ('TUE', 'Technische Universiteit Eindhoven'),
        ('IEID', 'Industrial Engineering & Innovation Sciences'),
        ('ST', 'Scheikundige Technologie'),
        ('TN', 'Technishe Natuurkunde'),
        ('wbtk', 'Werktuigboukunde'),
        ('WI', 'Wiskunde & Informatica')
    )
    faculty = models.CharField(choices=FACULTY_OPTIONS, max_length=4, default='BK')

    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.id + " " + self.name

    def getAverage(self):
        return "{0:.1f}".format(self.averageRating)


class Timeslot(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1, choices=((i, i) for i in 'abcdex'))
    quartile = models.CharField(max_length=2,
                                choices=tuple((str(i), str(i))
                                              for i in range(1, 5)))
    year = models.IntegerField()

    def __str__(self):
        return str(self.course) + " in " + str(self.year) + " Q" + str(self.quartile) + " timeslot " + str(
            self.letter).upper()


class Student(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True, on_delete=models.CASCADE)
    startYear = models.IntegerField()
    MAJOR_OPTIONS = (
        ('sfs', 'Software Science'),
        ('ws', 'Web Science'),
        ('id', 'Industrial Design')
        ('png', 'Psychology & Technology'),
        ('mwt', 'medishe wetenshappen en technologie'),
        ('ie' 'Industrial Engineering'),
        ('si', 'Sustainable Innovation'),
        ('ds', 'Data Science'),
        ('wtbk', 'Werktuigboukunde'),
        ('aubs', 'Bouwkunde'),
        ('au', 'Automotive Technology'),
        ('bmt', 'Biomedishe Technologie'),
        ('cec', 'Chemical Engineering & Chemisty'),
        ('cse', 'Computer Science en Engineering'),
        ('ntk', 'Applied Physics'),
        ('wis', 'Applied Mathematics'),
        ('ee', 'Electrical Engineering')
    )
    major = models.CharField(max_length=16, choices=MAJOR_OPTIONS)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    thumbsUp = models.ManyToManyField(Student, related_name="thumbsUp")
    thumbsDown = models.ManyToManyField(Student, related_name="thumbsDown")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reviewShort = models.CharField(max_length=200)
    reviewLong = models.TextField()
    date = models.DateField(default=timezone.now)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    ratingOverall = models.IntegerField(default=0)
    ratingInf = models.IntegerField(default=0)
    ratingTime = models.IntegerField(default=0)
    ratingRele = models.IntegerField(default=0)
    ratingDiff = models.IntegerField(default=0)
