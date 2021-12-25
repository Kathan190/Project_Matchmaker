from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cumber = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cname

class Year(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class SEyear(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class BMyear(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class CSyear1(models.Model):
    title = models.CharField(max_length=100)
    assignment_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.assignment_name

class CSyear2(models.Model):
    title = models.CharField(max_length=100)
    assignment_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.assignment_name

class CSyear3(models.Model):
    title = models.CharField(max_length=100)
    assignment_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.assignment_name


