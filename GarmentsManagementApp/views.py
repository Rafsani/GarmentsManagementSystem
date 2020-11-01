from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def admin_login(request):
    if request.method != 'POST':
        return render(request,'login.html')
    else:
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user_ref = authenticate(username=user_name,password=pass_word)
        if user_ref:
            if user_ref.is_active and user_ref.is_staff and not user_ref.is_superuser:
                login(request, user_ref)
                return redirect('/dashboard/')
            else:
                return HttpResponse("<h1> You are not authorized to view Dashboard</h1>")
        else:
            return HttpResponse("login failed")


@login_required(login_url='/login/')
def admin_logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request,'dashboard.html')
