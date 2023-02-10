from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
        user = User.objects.create_user(username=username,email=email,password=password,last_name=last_name)
        user.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('user_login')
    else:
        return render(request,'register.html')

def user_login(request):
    # if 'username' in request.session:
    #     return redirect(dashboard)
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            # request.session['username'] = username
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
        logout(request)
        return redirect('user_login')
    except:
        return redirect('user_login')
    return redirect('user_login')

    # if 'username' in request.session:
    #     request.session.flush()
    # return redirect('user_login')

def dashboard(request):
    # if 'username' in request.session:
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect(user_login)
# Create your views here.
