from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name=("main_page")),
]