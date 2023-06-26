from django.shortcuts import render,redirect
from .forms import UserRegisteration
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthorized_user
from django.views.generic import DetailView
# from django.contrib.auth.models import User
from .forms import User

def home(request):
    return render(request, 'userprofile/base.html')

@unauthorized_user
def userRegisteration(request):
    form =UserRegisteration()
    if request.method=='POST':
        form=UserRegisteration(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.info(request,username+'your account is created login to continue')
            return redirect('userprofile:login')

    context={'form':form}
    return render(request, 'userprofile/register.html', context)


@unauthorized_user
def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('forum:home')
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request, 'userprofile/login.html')

def userlogout(request):
    logout(request)
    return render(request, 'forum/index.html')

def forum(request):
    return render(request, 'userprofile/index.html')
@login_required(login_url='userprofile:login')
def profile(request):
    return render(request, 'userprofile/profile.html')

class NewsDetailView(DetailView):
    form = User()
    template_name = 'userprofile/profile.html'
    context_object_name = 'Users'
