from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
       ("Male", "Male"),
       ("Female", "Female"), 
    ]
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    image = models.ImageField(upload_to="profile_pics/", null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    