from django.apps import apps
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.views import APIView

from backend.models import Core


def index(request):
    coreModel = apps.get_model('backend', 'Core')
    user = User.objects.filter(id=request.user.id)
    if len(user) != 0:
        core = Core.objects.get(user=request.user)
        return render(request, 'main/index.html', {'core': core})
    else:
        return redirect('login')