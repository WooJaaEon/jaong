from django.urls import path
from . import views

# user id : tester
# password : 789456

urlpatterns = [
    path('',views.index, name = "index"),
    path('login',views.login_view, name = "login"),
    path("logout",views.logout_view, name = "logout")
]
