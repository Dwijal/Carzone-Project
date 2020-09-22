from django.shortcuts import render,redirect
from .models import Team
from cars.models import car
from django.contrib import messages 
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    m=Team.objects.all()
    featured_car=car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=car.objects.order_by('-created_date')

    # search_fields=car.objects.values('model','city','year','body_style')
    model_search=car.objects.values_list('car_title',flat=True).distinct()
    city_search=car.objects.values_list('city',flat=True).distinct()
    year_search=car.objects.values_list('year',flat=True).distinct()
    body_style_search=car.objects.values_list('body_style',flat=True).distinct()
    d={'team':m,'f':featured_car,'all':all_cars,'model_search':model_search,'city_search':city_search,'year_search':year_search,'body_style_search':body_style_search}
    return render(request,'pages/home.html',d)

def about(request):
    m=Team.objects.all()
    d={'team':m}
    return render(request,'pages/about.html',d)

def service(request):
    return render(request,'pages/service.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']

        email_subject=' You have a new message from Carzone website regarding ' + subject
        message_body=' Name :'  +  name +  '  Email :'  +  email + '  Phone :'  + phone  + '  Messages :'  + message
        admin_info=User.objects.get(is_superuser=True)
        admin_email=admin_info.email
        send_mail(
            'New Car Enquiry',
             message_body,
            'dwijal2019@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,'Thank you for contacting us...We will get back to you shortly')
        return redirect('contact')


    return render(request,'pages/contact.html')
