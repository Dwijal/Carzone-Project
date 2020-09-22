from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.

class carAdmin(admin.ModelAdmin):

    def thumbnail(s,object):

        return format_html('<img src="{}" width="40px" style="border-radius:40%"/>'.format(object.car_photo.url))

    list_display=['id','thumbnail','car_title','city','color','year','body_style','fuel_type','is_featured']
    list_display_links=['id','car_title']

    list_editable=['is_featured']

    search_fields=['car_title','city','fuel_type','color','body_style']
    list_filter=['body_style']
    


admin.site.register(car,carAdmin)