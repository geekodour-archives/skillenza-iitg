"""URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from .views import HomeView

urlpatterns = [
    url(r'', HomeView.as_view(), name='index'),
]
