from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(s,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50%"/>'.format(object.photo.url))

    list_display=['id','thumbnail','first_name','designation','created_date']

    list_display_links=['id','first_name']

    search_fields=['first_name','last_name','designation']

    list_filter=['designation',]

admin.site.register(Team,TeamAdmin)