from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# API_TITLE = 'Babies World API Documentation'
# API_DESCRIPTION = 'Babies World where you can shop and choose the best Care giver for your Baby'


urlpatterns = [
    path('', include('products.urls')),
    path('', include('tips.urls')),
    path('auth/', include('rest_framework.urls')),
    path('rest/', include('rest_auth.urls')),
    path('rest/reg/', include('rest_auth.registration.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
