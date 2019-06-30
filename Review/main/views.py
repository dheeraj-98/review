from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'main/index.html')

@login_required
def register(request):
    return render(request, 'main/register.html')

def login(request):
	if request.method=='POST':
		email=request.POST.get('email') 
		pwd=request.POST.get('password') 
		us=User.objects.filter(email=email)
		u_name=us[0].username
		print(u_name)
		
		user = authenticate(username=u_name,password=pwd)
		if user is not None:
			auth_login(request,user)
			return redirect('main-home')
		else:
			raise ValidationError("Wrong Credentials")
		 

	return render(request,'main/login.html')
