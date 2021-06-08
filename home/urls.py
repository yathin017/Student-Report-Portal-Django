from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('result',views.result,name='result'),
]
