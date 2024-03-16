from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import DataForm
from .models import Data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')
def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse('Your password & confirm password are not same')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('login')
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "<h1 style='font-family: Arial, sans-serif; font-size: 74px; color: red; text-align: center; margin-top: 290px;'>Username or Password is incorrect!!!</h1>"
            return HttpResponse (error_message)

    return render (request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predictions')
    else:
      form=DataForm()
    context={'form':form}    
    return render(request,'dashboard/index.html',context)
@login_required(login_url='login')
def predictions(request):
    predicted_grades=Data.objects.all()
    context={
        'predicted_grades':predicted_grades
    }
    print(predicted_grades)
    return render(request,'dashboard/predictions.html',context)    
def main(request):
    return render(request,'home.html')

