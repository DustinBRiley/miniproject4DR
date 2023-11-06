import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    creator = User.get_username
    creation_date = models.DateTimeField("date created")
    Name = models.CharField(max_length=200)
    Type = [
        ("Normal","Normal"),
        ("Electric","Electric"),
        ("Grass","Grass"),
        ("Poison","Poison"),
        ("Water","Water"),
        ("Ice","Ice"),
        ("Fire","Fire"),
        ("Bug","Bug"),
        ("Flying","Flying"),
        ("Rock","Rock"),
        ("Ground","Ground"),
        ("Fighting","Fighting"),
        ("Psychic","Psychic"),
        ("Ghost","Ghost"),
        ("Dragon","Dragon")
    ]
    Type1 = models.CharField(max_length=8, choices=Type)
    Type2 = models.CharField(max_length=8, choices=Type)
    Weakness = models.CharField(max_length=8, choices=Type)
    def __str__(self):
        return self.Name
    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)