from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import models
from .models import Register

def home(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        occupation = request.POST.get('occup')
        mail_id = request.POST.get('email')
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        print(pass_word,user_name,mail_id,occupation,full_name)
        user = User.objects.create(username=user_name,email=mail_id)
        user.set_password(pass_word)
        user.save()
        reg = Register.objects.create(name=full_name, occup=occupation, username=user_name)
        reg.save()
        #return render(request, 'main/login.html')
        return redirect('main-login')
    return render(request, 'main/register.html')

def login(request):
    context = {"msg":""}
    if request.method=='POST':
        user_name=request.POST.get('username')
        pwd=request.POST.get('password')
        us=User.objects.filter(username=user_name)
        if len(us) == 0:
            context["msg"] = "Wrong Credentials"
        else:
            u_name=us[0].username
            user = authenticate(username=u_name,password=pwd)
            if user is not None:
                auth_login(request,user)
                return redirect('main-home')
            else:
                context["msg"] = "Wrong Credentials"
    return render(request,'main/login.html', context)

@login_required
def write(request):
    return render(request, 'main/write.html')
