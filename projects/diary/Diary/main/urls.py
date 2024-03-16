from django.urls import path 
from . import views 

app_name = "main"

urlpatterns = [
    path("index/", views.index, name = "index"), #views.後面就是找views.py裡面的function, function不是在這裡叫, it's django who call the fun, we only need to tell django where the function is 
    path("signin/", views.signin, name= "signin"),
    path("signout/",views.signout, name="signout"),
    path("signup/", views.signup, name = "signup"),
    path("create/", views.create, name = "create"),
    path("update/<int:current_id>", views.update, name = "update") #可以去抓網址後面的id, id不可能重複, 不管跨不跨user (coz the same database)
]
