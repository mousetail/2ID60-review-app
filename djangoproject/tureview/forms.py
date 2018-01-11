from django import forms as dforms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Student

class RegistrationForm(dforms.Form):
    username = dforms.CharField(label='username')
    password = dforms.CharField(widget = dforms.PasswordInput, label='password')
    password_2 = dforms.CharField(widget=dforms.PasswordInput, label='confirm password')
    major = dforms.ChoiceField(label='major', choices=Student.MAJOR_OPTIONS)
    startyear = dforms.IntegerField(label='start year')

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password
