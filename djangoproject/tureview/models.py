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
    averageRating = models.FloatField()
    reviewNumber= models.IntegerField(default=0)

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
        return self.id + " "+self.name

    def getAverage(self):
        return "{0:.1f}".format(self.averageRating)


class Timeslot(models.Model):
    course = models.ForeignKey(Course)
    letter = models.CharField(max_length=1, choices=((i, i) for i in 'abcdex'))
    quartile = models.CharField(max_length=2,
                                choices=tuple((str(i), str(i))
                                              for i in range(1, 5)))
    year = models.IntegerField()

    def __str__(self):
        return str(self.course) + " in " + str(self.year) + " Q" + str(self.quartile) + " timeslot " + str(
            self.letter).upper()


class Student(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True)
    startYear = models.IntegerField()
    MAJOR_OPTIONS = (
        ('sfs', 'Software Science'),
        ('ws', 'Web Science'),
        ('ee', 'Electrical Engineering'),
        ('id', 'Industrial Design')
    )
    major = models.CharField(max_length=16, choices=MAJOR_OPTIONS)
    #THUMBS UP
    #THUMBS DOWN
    #MALE/FEMALE/APACHE???

    def __str__(self):
        return self.user.username


class Review(models.Model):
    student = models.ForeignKey(Student)
    reviewShort = models.CharField(max_length=200)
    reviewLong = models.TextField()
    date = models.DateField(default=timezone.now)
    timeslot = models.ForeignKey(Timeslot)

    ratingOverall = models.IntegerField(default=5)
    #GRADE
    #THUMBS UP
    #THUMBS DOWN
