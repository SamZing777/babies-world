from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
	def get_search_fields(self, view, request):
		if request.query_params.get('title_only'):
			return ['name']
		return super().get_search_fields(view, request)


class IsOwnerFilterBackend(filters.BaseFilterBackend):
	
	# Allows users only to see thier own objects

	def filter_queryset(self, request, queryset, view):
		return queryset.filter(owner=request.user)
