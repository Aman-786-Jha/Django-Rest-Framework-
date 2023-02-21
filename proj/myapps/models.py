from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    work = models.ManyToManyField('Work')

class Work(models.Model):
    LINK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(choices=LINK_TYPES, max_length=200)

    def __str__(self):
        return self.work_type 


