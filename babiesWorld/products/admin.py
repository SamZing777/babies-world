from django.contrib import admin

from .models import (
	ProductCategory,
	ProductSubCategory,
	Product
	)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'sub_category', 'free_shipping', 'price']


admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(Product, ProductAdmin)
