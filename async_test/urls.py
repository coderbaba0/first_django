# async_test/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('async-view/', views.async_view, name='async_view'),
]
