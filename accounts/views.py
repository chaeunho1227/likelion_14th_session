from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main:blogpage')
        else:
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:blogpage')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            username = request.POST['username']
            password = request.POST['password']
            
            new_user = User.objects.create_user(
                username = username,
                password = password
            )
            
            nickname = request.POST['nickname']
            major = request.POST['major']
            profile_image = request.FILES.get('profile_image')
            
            profile = Profile(
                user = new_user,
                nickname = nickname,
                major=major,
                profile_image=profile_image,
                
            )
            
            profile.save()
            
            auth.login(request, new_user)
            return redirect('main:blogpage')
            
    return render(request, 'accounts/signup.html')