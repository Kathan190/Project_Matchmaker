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