from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from djmoney.models.fields import MoneyField

User = get_user_model()


class ProductCategory(models.Model):
	name = models.CharField(max_length=25)
	slug = AutoSlugField(populate_from='name', always_update=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'Product Categories'


class ProductSubCategory(models.Model):
	category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, 
								related_name='sub_categories', null=True)
	name = models.CharField(max_length=25)
	slug = AutoSlugField(populate_from='name', always_update=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'Product Sub_Categories'


class Product(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,
							related_name='user_products')
	name = models.CharField(max_length=25)
	slug = AutoSlugField(populate_from='name', always_update=False)
	category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING,
								null=True, related_name='products')
	sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.DO_NOTHING, 
								blank=True, null=True, related_name='products_in')
	description = models.TextField()
	free_shipping = models.BooleanField(default=False)
	shipping_fee = MoneyField(max_digits=10, decimal_places=2, default_currency='USD',
							null=True, blank=True)
	price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
	timeStamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
