from django.contrib import admin
from django.urls import path,re_path,include
from django.contrib.auth.models import User


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("resumeapp.urls")),
]