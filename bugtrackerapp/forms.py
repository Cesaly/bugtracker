from django.forms import ModelForm
from django import forms
from .models import Ticket


class Ticketadd(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class Login(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(widget=forms.PasswordInput)


class Edit(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'ticket_status', 'ticket_assignee']


class Adduser(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)
