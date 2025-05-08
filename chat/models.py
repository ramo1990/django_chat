from django.db import models
from datetime import datetime

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Message(models.Model):
    # value = models.CharField(max_length=1000)
    # date = models.DateTimeField(default=datetime.now, blank = True)
    # user = models.CharField(max_length=1000)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank = True)
    user = models.CharField(max_length=1000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # room = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user}: {self.value[:20]}'