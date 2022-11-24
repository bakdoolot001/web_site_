from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from products.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include("products.urls")),
    path('', include("shop.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
