from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,UserRegistrationForm
from django.contrib import messages

def sign_in(request):
    if request.method =="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, f'Login request was successfull {user.username}')
                return redirect("art:product_list")
            
            else:
                messages.error(request, 'Invalid username or password')

                # return redirect("account:login")
    else:
        form=LoginForm()
    return render(request, 'account/login.html',{'form':form})
    

def sign_out(request):
    logout(request)
    messages.success(request, "Logout request was successfull")
    return redirect("product:product_list")
    


            
def sign_up(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            return render(request, "account/register_done.html",{'user':user})
    else:
        form=UserRegistrationForm()
    return render(request, 'account/register.html',{'form':form})

