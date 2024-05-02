from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms 


def user_signup(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "user logged in successfully!!")
            return redirect("home")
        else:
            for field, errors in form.items():
                for error in errors:
                    messages.error(request, f"{error} in {field}")
    else:
        form = forms.SignupForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def home(request):
    return render(request, "e_commerce/home.html")