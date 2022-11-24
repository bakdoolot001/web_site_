from django.contrib import admin

from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'last_name', 'phone1', 'address', 'profession', 'image']
    list_editable = ['phone1']
