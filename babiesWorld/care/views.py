from rest_framework import viewsets

from .filters import CareFilter

from .models import (
	BabyCareCategory,
	BabyCare,
	BabyHealth
	)

from .serializers import (
	BabyCareCategorySerializer,
	BabyCareSerializer,
	BabyHealthSerializer
	)


class BabyCareCategoryViewSet(viewsets.ModelViewSet):
	queryset = BabyCareCategory.objects.all()
	serializer_class = BabyCareCategorySerializer


class BabyCareViewSet(viewsets.ModelViewSet):
	queryset = BabyCare.objects.all()
	serializer_class = BabyCareSerializer

	filter_class = (
		CareFilter				# Defined filter using django_filters.rest_framework.FilterSet
	)
	ordering_fields = (
		'age'
	)


class BabyHealthViewSet(viewsets.ModelViewSet):
	queryset = BabyHealth.objects.all()
	serializer_class = BabyHealthSerializer
