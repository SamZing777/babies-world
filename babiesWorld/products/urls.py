from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
	ProductViewSet,
	ProductCategoryViewSet,
	ProductSubCategoryViewSet
	)

from care.views import (
	BabyCareCategoryViewSet,
	BabyCareViewSet,
	BabyHealthViewSet
	)


router = DefaultRouter()
router.register('baby-care-category', BabyCareCategoryViewSet)
router.register('baby-care', BabyCareViewSet)
router.register('baby-health', BabyHealthViewSet)
router.register('product-category', ProductCategoryViewSet)
router.register('product-sub-category', ProductSubCategoryViewSet)
router.register('products', ProductViewSet)


urlpatterns = [
	path('', include(router.urls))
]
