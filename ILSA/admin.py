from django.contrib import admin
from .models import Locker, Admin

class LockerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['card_uid']}),
        ('Date Information', {'fields': ['check_out_time'], 'classes': ['collapse']}),
    ]
    list_display = ('lock_num', 'card_uid', 'check_out_time', 'status')
    list_filter = ['check_out_time']

admin.site.register(Locker, LockerAdmin)

