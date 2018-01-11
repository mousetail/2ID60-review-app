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
    summary = dforms.CharField(widget=dforms.TextInput(
        attrs={'placeholder': 'A once-sentence summary of your review'}))
    content = dforms.CharField(widget=dforms.Textarea())
    year = dforms.IntegerField(label='year course taken', initial=2000, widget=dforms.NumberInput(
        attrs={'min': '1900', 'max': '2500'}
    ))
    quartile = dforms.ChoiceField(label="quartile course taken",
                                  choices=tuple((str(i), str(i))
                                                for i in range(1, 5)))
    letter = dforms.ChoiceField(label="timeslot",
                                choices=tuple((i, i) for i in 'abcdex')
                                )
