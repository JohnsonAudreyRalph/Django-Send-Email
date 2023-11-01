from django.contrib import admin
from .models import Email_Content

# Register your models here.
@admin.register(Email_Content)
class Email_Admmin(admin.ModelAdmin):
    list_display = ('id', 'User_name', 'User_email', 'create_day')