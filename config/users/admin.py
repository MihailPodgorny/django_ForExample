from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'last_name', 'first_name', 'second_name', 'phone', 'email', 'birth_date', 'dormitory', 'room')
    search_fields = ('last_name', 'phone', 'dormitory', 'room')
    ordering = ['last_name', 'first_name', 'second_name']


admin.site.register(User, UserAdmin)
