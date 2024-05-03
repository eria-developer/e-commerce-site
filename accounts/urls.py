from django.urls import path
from . import views
import django.contrib.auth.views as auth_views

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("signin/", views.user_signin, name="signin"),
    path("signout/", views.user_signout, name="signout"),
    path("password_change/", views.password_change, name="password_change"),
    path("password_change_done/", views.password_change_done, name="password_change_done"),
]

urlpatterns += [
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_complete")
]