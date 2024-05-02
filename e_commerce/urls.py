
from django.contrib import admin
from django.urls import path, include
import accounts, store

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls")),
    path("/", include("store.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
