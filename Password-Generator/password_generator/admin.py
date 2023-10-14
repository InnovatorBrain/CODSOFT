from django.contrib import admin
from .models import Password

@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'value')
    list_filter = ('length',)