from django.urls import path
from . views import *
urlpatterns=[
    path("", home, name="home1"),
    path("add", add, name="add")
    
]