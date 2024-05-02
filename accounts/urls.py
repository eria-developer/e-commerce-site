from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("signin/", views.user_signin, name="signin"),
    path("signout/", views.user_signout, name="signout"),
    path("password_change/", views.password_change, name="password_change"),
    path("password_change_done/", views.password_change_done, name="password_change_done"),
]