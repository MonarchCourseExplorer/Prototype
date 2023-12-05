from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

def test(request):
    return render(request,'test.html')

def test_two(request):
    return render(request,'authenticate/test2.html')

def test_three(request):
    return render(request,'authenticate/test3.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There Was An Error Logging In, Please Try Again"))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

def login_faculty_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There Was An Error Logging In, Please Try Again"))
            return redirect('flogin')

    else:
        return render(request, 'authenticate/faculty_login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ('You have registered...'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'authenticate/register.html', context)