from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.urls import reverse


# Create your models here.
class MyUser(AbstractUser):
    displayname = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['displayname']


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(MyUser,related_name="author", on_delete=models.CASCADE)
    NEW = 'n'
    IN_PROGRESS = 'ip'
    FINISHED = 'f'
    INVALID = 'iv'
    ticket_status_choices = [
        ['New', 'New'],
        ['In Progress', 'In Progress'],
        ['Done', 'Done'],
        ['Invaild', 'Invalid'],
    ]
    ticket_status = models.CharField(max_length=2, choices=ticket_status_choices, default=NEW)
    ticket_assignee = models.ForeignKey(MyUser, null=True, related_name='ticketassignee', on_delete=models.CASCADE)
    ticket_finisher = models.ForeignKey(MyUser, related_name='ticketfinisher', null=True, on_delete=models.CASCADE)
