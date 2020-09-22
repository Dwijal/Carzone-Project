
from django.contrib import admin
from django.urls import path
from accounts import views as v

urlpatterns = [
    path('login',v.login_view,name='login_view'),
    path('logout',v.logout_view,name='logout_view'),
    path('register',v.register_view,name='register_view'),
    path('dashboard',v.dashboard_view,name='dashboard_view'),
    
]


 