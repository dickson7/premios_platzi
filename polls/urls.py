from operator import index
from unicodedata import name
from django.urls import path

from polls import views

urlpatterns = [
    path("", views.index, name="index"),
]