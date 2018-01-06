from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Course)
admin.site.register(models.Timeslot)
admin.site.register(models.Teacher)