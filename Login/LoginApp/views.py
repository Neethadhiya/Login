from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        repeat_pswd=request.POST['repeat_pswd']
        if password!=repeat_pswd:
            messages.error(request,"Password do not match")
            return redirect('register')
        user = User.objects.create_user(username,email,password)
        user.last_name = last_name
        user.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('user_login')
    else:
        return render(request,'register.html')
def user_login(request):
    if 'username' in request.session:
        return redirect(dashboard)
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                request.session['username'] = username
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Invalid Credentials, Please try again")
                return redirect('user_login')
        else:
            return render(request,'login.html')  
def user_logout(request):
    try:
        # del request.session['username']
        request.session.flush()
        logout(request)
    except:
        return redirect('user_login')
    return redirect('user_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def dashboard(request):
    # if request.user.is_authenticated:
    if 'username' in request.session:
        return render(request,'dashboard.html')
    else:
        return redirect(user_login)
# Create your views here.
