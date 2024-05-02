from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    