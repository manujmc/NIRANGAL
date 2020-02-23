from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from django.forms.fields import DateField
# from django.forms import extras
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput())

    class Meta():
        model = UserProfileInfo
        fields = ('gender','date_of_birth','phone','portfolio_site', 'profile_pic')

