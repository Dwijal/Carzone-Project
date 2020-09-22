
from django.contrib import admin
from django.urls import path
from contacts import views as v

urlpatterns = [
   path('enquiry',v.enquiry,name='enquiry'),
]


