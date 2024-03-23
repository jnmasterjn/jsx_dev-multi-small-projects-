from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import Diary, Color
from django.contrib.auth import authenticate,login,logout
from .form import DiaryForm

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
            User.objects.create_user(username = username,password = password).save() #save = 創造
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

def create (request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin"))
    
    if request.method == "POST":
        new_title = request.POST["title"]
        new_color = request.POST["color"]
        new_body = request.POST["body"]
        
        if new_color == "":
            Diary(user = request.user, title = new_title, body = new_body).save()
        
        else:
            new_color = Color.objects.get(color = new_color)
            Diary(user = request.user,
                  title = new_title,
                  body = new_body,
                  color = new_color).save()
            
        return redirect(reverse_lazy("main:index"))
    
    colors = Color.objects.all()
    diary_form = DiaryForm() #make object, empty 
    
    return render(request, "main/create.html", {
        "form": diary_form,
        "colors": colors,
    })

def update(request,current_id):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin"))
    
    #update diary stuff
    if request.method == "POST":
        new_title = request.POST["title"] #"title"跟html的tag name 一樣
        new_color = request.POST["color"]
        new_body = request.POST["body"]

        Diary.objects.filter(id = current_id, user = request.user).update(title = new_title)
        Diary.objects.filter(id = current_id, user = request.user).update(body = new_body)

        if new_color != "" and new_color is not None:   #updating color is more special cos the user might choose to change color to no color, hence we need to check before updating. 
            new_color = Color.objects.get(color = new_color)
            Diary.objects.filter(id = current_id, user = request.user).update(color = new_color)
        else:
            Diary.objects.filter(id = current_id, user = request.user).update(color = None)

        return redirect(reverse_lazy("main:index"))

    #給user所有他們可以modify的東西
    diary = Diary.objects.get(id = current_id, user = request.user)
    color = Color.objects.all() #they can access to all color
    form = DiaryForm(instance=diary) #空白的位置有之前的日記, not empty

    if form.is_valid():
        form.save() #if have instance, need "save" to change.

    #return diary, color, form stuff so user can update about them
    return render(request, "main/update.html", {
        "diary": diary,
        "colors": color,
        "form": form,
        #name : value
    })

def delete(request,current_id):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy("main:signin"))
    
    if request.method == "POST":
        Diary.objects.get(id = current_id, user = request.user).delete()
        return redirect(reverse_lazy("main:index"))
        

    return render(request, "main/delete.html")