import django_filters
from django_filters import (
	AllValuesFilter,
	DateTimeFilter,
	NumberFilter
	)


from .models import BabyCare


class CareFilter(django_filters.rest_framework.FilterSet):
	minimum_age = NumberFilter(
		field_name='age', lookup_expr='gte'
		)
	maximum_age = NumberFilter(
		field_name='age', lookup_expr='lte'
		)
	category = AllValuesFilter(
		field_name='care__name'
		)

	class Meta:
		model = BabyCare
		fields = (
			'minimum_age',
			'maximum_age',
			'category'
		)
