from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .sitemaps import WorkSitemap, ServiceSitemap, CategorySitemap, StaticViewSitemap
from apps.main.views import robots_txt

sitemaps = {
    'works': WorkSitemap,
    'services': ServiceSitemap,
    'categories': CategorySitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('gest/', admin.site.urls),

    # SECTION - Apps
    path('', include('apps.main.urls')),

    # SECTION - INCLUDES
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)