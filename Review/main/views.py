from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')
def login(request):
    return render(request, 'main/login.html')
def register(request):
    return render(request, 'main/register.html')
