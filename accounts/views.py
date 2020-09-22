from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'You are logined successfully')
            return redirect('dashboard_view')
        else:
            messages.error(request,'Wrong Username or password')
            return redirect('login_view')

    

    
    
    return render(request,'accounts/login.html')


def register_view(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'User already exists...Please try different')
                return redirect('register_view')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exist... Please try different')
                    return redirect('register_view')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password)
                    user.save()
                    messages.success(request,'You are successfully registered')
                    return redirect('login_view')
        else:
            messages.error(request,'Password does not match...Try again')
            return redirect('register_view')
        
    else:
        return render(request,'accounts/register.html')
@login_required(login_url='login_view')
def dashboard_view(request):
    user_inquiry=Contact.objects.order_by('create_date').filter(user_id=request.user.id)
    data={
        'inquiry':user_inquiry
    }
    return render(request,'accounts/dashboard.html',data)

def logout_view(request):
    messages.success(request,'Your are logout successfully')
    logout(request)
    return redirect('login_view')