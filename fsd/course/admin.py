from django.contrib import admin
from .models import Page
from django.contrib import admin
from . import models
from .models import *

admin.site.register(Assignment)
admin.site.register(Aquestions)
admin.site.register(Video)
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['pfname','plname','pmobile','pcollege','page','user']
admin.site.register(Quizz)
admin.site.register(Topic)
admin.site.register(FilesAdmin)
admin.site.register(Post)
admin.site.register(Comment)
