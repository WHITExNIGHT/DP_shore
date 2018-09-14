from django.contrib import admin
from .models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'uname', 'unickname', 'uemail', 'utime', 'uaddress', 'uphone', 'upwd']
