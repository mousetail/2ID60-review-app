from django.db import models
from django.utils import timezone
# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length = 30)

class Course(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    descriptionShort = models.CharField(max_length=200)
    descriptionLong = models.TextField()
    
    course = models.ManyToManyField(Teacher)

class Timeslot(models.Model):
    course = models.ForeignKey(Course)
    letter = models.CharField(max_length=1, choices=((i,i) for i in 'abcdex'))
    quartile = models.CharField(max_length=2,
                                choices=tuple((str(i), str(i))
                                              for i in range(1,5)))
    year = models.IntegerField()

class Student(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True)
    startYear=models.IntegerField()
    MAJOR_OPTIONS = (
        ('sfs', 'Software Science'),
        ('ws', 'Web Science'),
        ('ee', 'Electrical Engineering'),
        ('id', 'Industrial Design')
        )
    major = models.CharField(max_length = 16)

class Review(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    reviewShort = models.CharField(max_length=200)
    reviewLong = models.TextField()
    date = models.DateField(default=timezone.now)
    timeslot = models.ForeignKey(Timeslot)


