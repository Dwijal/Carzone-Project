from django.contrib import admin
from contacts.models import Contact
# Register your models here.
class Contactadmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','car_title','phone','create_date']
    list_display_links=['id','first_name']
    list_per_page=15
    search_fields=['first_name','last_name','car_title']

admin.site.register(Contact,Contactadmin)