from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import Note

User = get_user_model()


def index(request):
    return render(request, 'register.html')


def register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    if username and password:
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect(request, 'login')


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    if username and password:
        user = authenticate(request, username, password)
        if user:
            login(request)
            return redirect('notes')
        
    return redirect(request, 'login')



class NoteView(View):
    def get(self, request):
        notes = Note.objects.all()
        
        return render(request, 'notes.html', context={"notes": notes})