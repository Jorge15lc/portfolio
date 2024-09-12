from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.main.models import Work, Service, Category

class WorkSitemap(Sitemap):
    changefreq = "weekly"  # Frecuencia de cambios en el contenido
    priority = 0.8  # Prioridad de la página en el sitemap

    def items(self):
        return Work.objects.all()  # Devuelve todos los trabajos

    def lastmod(self, obj):
        return obj.modified  # Utiliza la fecha de modificación del objeto Work

class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Service.objects.all()

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Agregar las vistas estáticas que quieres incluir en el sitemap
        return ['main:home', 'main:about', 'main:contact']

    def location(self, item):
        return reverse(item)