from django.contrib import admin
from django.urls import path, include
from . import views

boosts = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
lonely_boost = views.BoostViewSet.as_view({
     'put' : 'patrial_update'
 })
urlpatterns = [

    path('call_click/', views.call_click),
    path('boosts/', boosts, name= 'boosts'),
    path('boost/<int:pk>/', lonely_boost, name='boost')
]