from django.shortcuts import render,get_object_or_404
from cars.models import car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def cars(request):
    c=car.objects.order_by('-created_date')
    paginator=Paginator(c,4)
    page=request.GET.get('page')
    paged_car=paginator.get_page(page)

    model_search=car.objects.values_list('car_title',flat=True).distinct()
    city_search=car.objects.values_list('city',flat=True).distinct()
    year_search=car.objects.values_list('year',flat=True).distinct()
    body_style_search=car.objects.values_list('body_style',flat=True).distinct()

    d={'car':paged_car ,'model_search':model_search,'city_search':city_search,'year_search':year_search,'body_style_search':body_style_search}
    return render(request,'cars/cars.html',d)

def cars_detail(request,id):
    cd=get_object_or_404(car,pk=id)

    d={'cd':cd}
    return render(request,'cars/cars_detail.html',d)

def search(request):
    sc=car.objects.order_by('-created_date')
    model_search=car.objects.values_list('car_title',flat=True).distinct()
    city_search=car.objects.values_list('city',flat=True).distinct()
    year_search=car.objects.values_list('year',flat=True).distinct()
    body_style_search=car.objects.values_list('body_style',flat=True).distinct()
    transmisson=car.objects.values_list('transmission',flat=True).distinct()


    

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            sc=sc.filter(description__icontains=keyword)

    
    if 'car_title' in request.GET:
        car_title=request.GET['car_title']
        if car_title:
            sc=sc.filter(car_title__iexact=car_title)

     
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            sc=sc.filter(city__iexact=city)
        
      
    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            sc=sc.filter(year__iexact=year)

        
    if 'body_style' in request.GET:
        body_style=request.GET['body_style']
        if body_style:
            sc=sc.filter(body_style__iexact=body_style)

    if 'min-price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            sc=sc.filter(price__gte=min_price,price__lte=max_price)
    d={'sc':sc,'model_search':model_search,'city_search':city_search,'year_search':year_search,'body_style_search':body_style_search,'transmission':transmisson}

    return render(request,'cars/search.html',d)