from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from apps.main import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # SECTION - Apps
    path('', include('apps.main.urls')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)