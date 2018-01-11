from django import forms as dforms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Student, Timeslot


class RegistrationForm(dforms.Form):
    username = dforms.CharField(label='username')
    password = dforms.CharField(widget=dforms.PasswordInput, label='password')
    password_2 = dforms.CharField(widget=dforms.PasswordInput, label='confirm password')
    major = dforms.ChoiceField(label='major', choices=Student.MAJOR_OPTIONS)
    startyear = dforms.IntegerField(label='start year')

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password


class ReviewForm(dforms.Form):
    def __init__(self, timeSlotOptions, *args, **kwargs):
        dforms.Form.__init__(self, *args, **kwargs)
        self.fields["timeslot"].choices = timeSlotOptions
    summary = dforms.CharField(widget=dforms.TextInput(
        attrs={'placeholder': 'A once-sentence summary of your review'}))
    content = dforms.CharField(widget=dforms.Textarea())
    year = dforms.IntegerField(label='year course taken', initial=2000, widget=dforms.NumberInput(
        attrs={'min': '1900', 'max': '2500'}
    ))
    timeslot = dforms.ChoiceField(label='quartile taken', choices=())
    def clean_timeslot(self):
        slot = self.cleaned_data['timeslot'].split(',')
        return slot
