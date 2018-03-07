from django.contrib import admin
from .models import Locker, Admin

class LockerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['lock_num', 'unlockable']}),
        ('Date Information', {'fields': ['check_out_time'], 'classes': ['collapse']}),
    ]
    list_display = ('lock_num', 'status', 'unlockable', 'battery_level', 'check_out_time')
    readonly_fields = ['battery_level']
    list_filter = ['check_out_time']

class AdminPage(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['admin_uid']}),
    ]
    list_display = ('name', 'admin_uid')

admin.site.register(Locker, LockerAdmin)
admin.site.register(Admin, AdminPage)
