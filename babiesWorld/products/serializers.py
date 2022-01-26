from rest_framework import serializers

from .models import (
	ProductCategory,
	ProductSubCategory,
	Product
	)


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='name'
	)
	sub_categories = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='name'
	)

	class Meta:
		model = ProductCategory
		fields = ['name', 'products', 'sub_categories']


class ProductSubCategorySerializer(serializers.HyperlinkedModelSerializer):

	products_in = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='name'
	)

	class Meta:
		model = ProductSubCategory
		fields = ['name', 'category', 'products_in']


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = '__all__'




"""
***** Slug Related Field
		sub_categories = serializers.SlugRelatedField(
				many=True,
				read_only=True,
				slug_field='name'
			)
*****

***** HyperlinkedRelatedField
		products_in = serializers.HyperlinkedRelatedField(
				many=True,
				read_only=True,
				view_name='productsubcategory-detail'
			)
*****


['user', 'name', 'category', 'sub_category', 'description',
				 'free_shipping', 'price', 'timeStamp', 'slug']


	def create(self, validated_data):
		return Product.objects.create(**validated_data)


	def update(self, instance, validated_data):
		instance.category = validated_data.get('category', instance.category)
		instance.sub_category = validated_data.get('sub_category', instance.sub_category)
		instance.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.free_shipping = validated_data.get('free_shipping', instance.free_shipping)
		instance.shipping_fee = validated_data.get('shipping_fee', instance.shipping_fee)
		instance.price = validated_data.get('price', instance.price)
		instance.save()
		return instance
"""
