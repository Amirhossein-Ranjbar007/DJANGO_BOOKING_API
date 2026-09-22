from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'date_joined']
    list_filter = ['is_staff']
    search_fields = ['email', 'phone']
    ordering = ['date_joined']


admin.site.register(User, UserAdmin)

