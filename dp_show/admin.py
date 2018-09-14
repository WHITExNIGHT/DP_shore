from django.contrib import admin

from dp_show.models import *


@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']


@admin.register(ImgInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'ititle', 'iclick', 'ipraise', 'itime', 'iuser', 'itype']
