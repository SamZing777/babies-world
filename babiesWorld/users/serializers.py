from django.contrib.auth import get_user_model
from rest_framework import serializers

from products.models import Product

User = get_user_model()


class UserProductSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Product
		fields = [
			'url',
			'name',
			'price',
			'shipping_fee_currency',
			'free_shipping'
		   ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
	user_products = UserProductSerializer(
		many=True,
		read_only=True
		)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'user_products'
		]
