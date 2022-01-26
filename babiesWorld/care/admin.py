from django.contrib import admin

from .models import (
	BabyCareCategory,
	BabyCare,
	BabyHealth
	)

class BabyCareAdmin(admin.ModelAdmin):
	list_display = ['agent_full_name', 'gender', 'title']


class BabyHealthAdmin(admin.ModelAdmin):
	list_display = ['title', 'full_name', 'gender', 'ratings']


admin.site.register(BabyCareCategory)
admin.site.register(BabyCare, BabyCareAdmin)
admin.site.register(BabyHealth, BabyHealthAdmin)
