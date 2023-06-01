from django.urls import path
from . import views
from .views import Login, Register

urlpatterns = [

    path('login/', Login.as_view(), name='login'),
    path('registration/', Register.as_view(), name='registration'),
    path('logout/', views.user_logout, name = 'logout'),


]
