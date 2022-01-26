from django.urls import path

from .views import (
	TipListAPIView,
	TipDetailAPIView
	)


urlpatterns = [
	path('tips/', TipListAPIView.as_view(), name='tips'),
	path('tips/<int:pk>/', TipDetailAPIView.as_view(), name='tip-detail')

]
