from django.shortcuts import render, redirect, get_object_or_404
from . import models


def home(request):
    categories = models.Category.objects.all()
    products_by_category = {}

    for category in categories:
        products_by_category[category] = models.Product.objects.filter(category=category)
    context = {
        "categories": categories,
    }
    return render(request, "store/home.html", context)


def products_by_category(request, id):
    category = get_object_or_404(models.Category, id=id)
    products = models.Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products,
    }
    return render(request, "store/products_by_category.html", context)


def my_account(request):
    return render(request, "store/my_account.html")