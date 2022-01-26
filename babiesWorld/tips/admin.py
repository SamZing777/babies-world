from django.contrib import admin

from .models import HealthTipsForBaby


class TipAdmin(admin.ModelAdmin):
	list_display = ['author', 'title', 'is_featured']


admin.site.register(HealthTipsForBaby, TipAdmin)
