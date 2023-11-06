import datetime

from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    creation_date = models.DateTimeField("date created")
    Name = models.CharField(max_length=200)
    Type1 = [
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
    Type2 = [
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
    Weakness = [
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
    def __str__(self):
        return self.Name
    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)