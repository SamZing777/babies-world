from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import (
	BabyCareCategory,
	BabyCare,
	BabyHealth
	)


class BabyCareSerializer(serializers.ModelSerializer):

	class Meta:
		model = BabyCare
		fields = '__all__'


class BabyCareCategorySerializer(serializers.ModelSerializer):
	baby_care = BabyCareSerializer(many=True, read_only=True)

	class Meta:
		model = BabyCareCategory
		fields = ['name', 'baby_care']


class BabyHealthSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = BabyHealth
		fields = '__all__'


"""
class BabyHealthHyperlinkedSerializer(serializers.HyperlinkedRelatedField):
	view_name = 'babycare-detail'
	queryset = BabyCare.objects.all()

	def get_url(self, obj, view_name, request, format):
		url_kwargs = {
			'babycare_slug': obj.babycare.slug,
			'babycarecategory_pk': obj.pk
		}
		return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

	def get_object(self, view_name, view_args, view_kwargs):
		lookup_kwargs = {
			'babycare_slug': view_kwargs['babycare_slug'],
			'pk': view_kwargs['babycarecategory_pk']
		}
		return self.get_queryset().get(**lookup_kwargs)
"""
