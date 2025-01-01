from django.urls import path
from . views import *
urlpatterns=[
    path("register", register, name="registration"),
    path('login',login,name="login"),
    path("logout", logout, name="logout"),
    path("pune", pune, name="pune")

    
]