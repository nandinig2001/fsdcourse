from django.contrib import admin
from .models import Page
from django.contrib import admin
from . import models
from .models import Assignment
admin.site.register(Assignment)
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['pfname','plname','pmobile','pcollege','page','user']
