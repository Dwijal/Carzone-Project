
from django.contrib import admin
from django.urls import path
from pages import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home,name='home'),
    path('about',v.about,name='about'),
    path('service',v.service,name='service'),
    path('contact',v.contact,name='contact'),
]
