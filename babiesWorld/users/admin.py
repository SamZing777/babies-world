from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'date_joined', 'is_active', 'email']


admin.site.register(User, UserAdmin)

"""
	Username: Admin
	Password: babiesAdmin123
"""
