from django.contrib import admin

from .models import Dormitory, Room


class DormitoryAdmin(admin.ModelAdmin):
    ordering = ['number']


class RoomAdmin(admin.ModelAdmin):
    ordering = ['dormitory', 'number', 'floor']


admin.site.register(Dormitory, DormitoryAdmin)
admin.site.register(Room, RoomAdmin)
