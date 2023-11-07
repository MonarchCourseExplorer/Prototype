from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

def test(request):
    return render(request,'test.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('test')
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There Was An Error Logging In, Please Try Again"))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

#def home(request):
    #return render(request, 'pages/gallery.html')
def logout_user(request):
    logout(request)
    return redirect('test')

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
            return redirect('test')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'authenticate/register.html', context)