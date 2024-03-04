from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import Diary, Color
from django.contrib.auth import authenticate,login,logout

def index(request): #所有使用者cookie session 包起來
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin")) #找main裡面的urls.py
    
    search_input = request.GET.get("search-area") or "" #把search area後面的(我們搜尋的東西)抓出來
    
    if search_input: #如果search-area後面有東西
        diarys = Diary.objects.filter(user=request.user,
                                      title__icontains = search_input)

    else: #如果search-area後面沒有東西
        diarys = Diary.objects.filter(user=request.user) #filter的條件是你只能看到自己的diary 要login

    return render(request, "main/index.html",{
        "diarys": diarys,
    })

#有登入才會跑以下
def signin(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("main:index"))

    error = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #user的 用戶名 and 密碼 已經被存到這兩個參數裡面了
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            pass
            login(request,user)
            return redirect(reverse_lazy("main:index")) #index就是urls.py裏面name取的名字
        else:
            error = True

    return render(request, "main/signin.html", {
        "error": error #這個"error"是對到signin html 語法的error; 前面是變數的名字 冒號後面是名字對到的value
    })

def signup(request):
    error = False

    if request.user.is_authenticated:
        return redirect (reverse_lazy('main:index'))

    if request.method == "POST":
        username = request.POST["username"] #"username"是input標籤的名字 這個input stuff會打在html 
        password = request.POST['password']
        re_password = request.POST['re_password']

        #一些篩選條件才能讓user創新帳號
        if username == "" or password == "" or re_password == "": #欄位不可以空
            error = "Please fill every box"
        
        elif password != re_password:
            error = "Passwords don't match"

        elif len(User.objects.filter(username = username))!= 0: #no duplicate usernames
            error = "Username already exsist"

        else:
            User.objects.create_user(username = username,password = password).save()
            return redirect (reverse_lazy("main:signin")) #如果創好帳號了就回去登入畫面

    return render(request, "main/signup.html",{
        "error": error
    })
    
    #return redirect(reverse_lazy("main:signin"))
    #if the user is alr signin and still wanna make a new acc, we redict him back to the signin page
    #reverse lazy 可以只給名字 不用講什麼html reverse lazy會幫你直接找urls.py裡面的name




def signout(request):
    if request.user.is_authenticated:  
        logout(request)
    return redirect(reverse_lazy("main:signin"))  #signin 完之後要回到signin頁面

