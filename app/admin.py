from django.contrib import admin
from .models import UserRegisterModel
# Register your models here.

@admin.register(UserRegisterModel)
class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ['id','Name','DOB','Email','Phone_number']