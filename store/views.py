from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    return render(request, "store/home.html")


def my_account(request):
    return render(request, "store/my_account.html")