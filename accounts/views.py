from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from accounts.models import UserProfile

def index(request):
    return create_account(request)

def create_account(request):
    def render_page(user_exists=False):
        params = {'user_exists': user_exists}
        return render(request, 'accounts/create_account.html', params)
        
    if request.method == 'POST':
        print('creating account')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        if User.objects.filter(username__iexact=username).exists() or User.objects.filter(email__iexact=email).exists():
            return render_page(user_exists=True)
        else:
            user = User.objects.create_user(username, email, password)
            profile = UserProfile.create(user)
            profile.save()
            return redirect('main.views.home')
    else:
        return render_page()
        alert
        
def login(request):
    def render_page(invalid_login=False):
        params = {'invalid_login': invalid_login}
        return render(request, 'accounts/login.html', params)
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main.views.home')
        else:
            return render_page(invalid_login=True)
    else:
        return render_page()
        
def logout(request):
    auth_logout(request)
    return redirect('main.views.home')

def setup(request):
    u = User.objects.create_user(username='default', email='default@yahoo.com', password='password')
    u.save()
    prof = UserProfile.create(user=u)
    prof.save()
    return HttpResponse('Successful database setup')
