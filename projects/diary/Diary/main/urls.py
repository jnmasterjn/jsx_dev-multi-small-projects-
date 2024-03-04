from django.urls import path 
from . import views 

app_name = "main"

urlpatterns = [
    path("index/", views.index, name = "index"), #views.後面就是找views.py裡面的function
    path("signin/", views.signin, name= "signin"),
    path("signout/",views.signout, name="signout"),
    path("signup/", views.signup, name = "signup") 
]
