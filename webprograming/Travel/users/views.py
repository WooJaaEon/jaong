from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def index(request):
    # login 안된 사용자이면 login 폼을 띄우고, login 된 사용자이면 welcome 이라고 인사
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # 사용자 이름과 암호가 올바른지 확인하고, 맞으면 사용자 개체를 반환
        user = authenticate(request, username=username, password=password)
        
        # 사용자 객체가 반환되면 로그인하고 인덱스 페이지로 라우트
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # 그렇지 않으면 새 컨텍스트로 로그인 페이지를 다시 반환
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
                "message": "Logged Out"
            })