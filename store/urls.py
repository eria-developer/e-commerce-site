from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("my_account", views.my_account, name="my_account"),
]
