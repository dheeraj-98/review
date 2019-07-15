from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="main-home"),
    path('login/', views.login, name="main-login"),
    path('register/', views.register, name="main-register"),
    path('write/', views.write, name="main-write"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
