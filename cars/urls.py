
from django.contrib import admin
from django.urls import path
from cars import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.cars,name='cars'),
    path('<int:id>',v.cars_detail,name='cars_detail'), 
    path('search',v.search,name='search'),
]


