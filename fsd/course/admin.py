from django.contrib import admin
from .models import Page
from django.contrib import admin
from . import models
from .models import *
admin.site.register(Assignment)
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['pfname','plname','pmobile','pcollege','page','user']
admin.site.register(Quizz)
admin.site.register(Topic)
