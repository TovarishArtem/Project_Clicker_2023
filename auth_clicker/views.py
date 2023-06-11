from django.apps import apps
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.views import APIView

from backend.models import Core
from .forms import UserForm
from .serializers import UserSerializer, UserSerializerDetail


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    user = User.objects.filter(id=request.user.id)
    if len(user)!= 0:
        coreModel = apps.get_model('backend', 'Core')
        boostsModel = apps.get_model('backend', 'Boost')
        core = coreModel.objects.get(user=request.user)
        boosts = boostsModel.objects.filter(core=core)
        return render(request, 'index.html', {'core': core,'boosts': boosts })
    else:
        return redirect('login')
class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerDetail


class Login(APIView):

    def get(self, request):
        return render(request, 'main/login.html', {'invalid': False})

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'main/login.html', {'invalid': True})


def user_logout(request):
    logout(request)
    return redirect('login')


class Register(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'main/registration.html', {'invalid': False, 'form': form})

    def post(self, request):
        coreModel = apps.get_model('backend', 'Core')
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            existing_user = User.objects.filter(username=username)
            if len(existing_user) == 0:
                password = form.cleaned_data['password']
                user = User.objects.create_user(username, '', password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                core = coreModel(user=user)

                core.save()
                return redirect('index')
            else:
                return render(request, 'main/registration.html', {'invalid': True, 'form': form})
