# This file is used to define the URL patterns for the project.
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
