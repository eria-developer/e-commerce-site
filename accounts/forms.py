from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . import models

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.CustomUser
        fields = ["username","firstname", "lastname", "email", "gender"]