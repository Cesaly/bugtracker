from django.forms import ModelForm
from django import forms
from bugtracker.models import Ticket
from django.contrib.auth.models import MyUser
from bugtracker import views

class Ticketadd(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class Login(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  3)

class Edit(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class Adduser(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)
