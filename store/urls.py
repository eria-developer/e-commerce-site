from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("my_account", views.my_account, name="my_account"),
    path("products_by_category/<int:id>", views.products_by_category, name="products_by_category"),
]
