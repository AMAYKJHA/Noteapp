from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Note

User = get_user_model()


def index(request):
    if request.user.is_authenticated:
        return redirect('notes')
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already exists'})
            
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
    
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('notes')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')


@method_decorator(login_required(login_url='login'), name='dispatch')
class NoteView(View):
    def get(self, request):
        notes = Note.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'notes.html', context={"notes": notes})
    
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if content:
            Note.objects.create(
                user=request.user,
                title=title if title else 'Untitled',
                content=content
            )
        
        return redirect('notes')