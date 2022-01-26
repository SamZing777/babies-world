from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework import (
	viewsets,
	filters,
	permissions,
	throttling
	)
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
	ProductCategory,
	ProductSubCategory,
	Product
	)

from .serializers import (
	ProductSerializer,
	ProductCategorySerializer,
	ProductSubCategorySerializer
	)

from .filters import CustomSearchFilter			# defined filter using rest_framework filters
from .permissions import IsOwnerOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	throttle_scope = 'products'
	throttle_classes = (throttling.ScopedRateThrottle,)

	filter_fields = (
		'name',
		'free_shipping',
		'price'

	)

	search_fields = (
		'name',
	)

	ordering_fields = (
		'name'          #  ----> '-timeStamp' can be used for "recent lists".
	)

	permission_classes = [
		permissions.IsAuthenticatedOrReadOnly,
		IsOwnerOrReadOnly
	]

	def perform_create(self, serializer):
		serializer.save(self, user=self.request.user)


class ProductCategoryViewSet(viewsets.ModelViewSet):
	queryset = ProductCategory.objects.all()
	serializer_class = ProductCategorySerializer
	filter_backends = [
		DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter
	]
	filterset_fields = [
		'name'
	]
	search_fields = ['name']
	ordering_fields = ['name']
	permission_classes = [
		permissions.IsAuthenticatedOrReadOnly
	]


class ProductSubCategoryViewSet(viewsets.ModelViewSet):
	queryset = ProductSubCategory.objects.all()
	serializer_class = ProductSubCategorySerializer
	filter_backends = [
		DjangoFilterBackend,
		filters.OrderingFilter,
		CustomSearchFilter
	]
	filterset_fields = [
		'category', 'name'
	]
	search_fields = ['name']
	ordering_fields = ['name']
	permission_classes = [
		permissions.IsAuthenticatedOrReadOnly
	]
