from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="main-home"),
    path('login/', views.login, name="main-login"),
    path('register/', views.register, name="main-register"),
]
