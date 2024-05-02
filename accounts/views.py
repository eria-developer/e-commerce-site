from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
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


def user_signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in successfully!!!")
                return redirect("home")
            else:
                messages.error(request, "Please check your username or password!!!")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signin.html")