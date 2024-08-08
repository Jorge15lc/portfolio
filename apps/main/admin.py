from django.contrib import admin
from .models import Work, Category, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = Work.gallery_images.through
    extra = 1

class WorkAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]

admin.site.register(Work, WorkAdmin)
admin.site.register(Category)
admin.site.register(GalleryImage)