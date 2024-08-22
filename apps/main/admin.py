from django.contrib import admin
from .models import Work, Category, GalleryImage, Service


class GalleryImageInline(admin.TabularInline):
    model = Work.gallery_images.through
    extra = 1

class WorkAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]

admin.site.register(Work, WorkAdmin)
admin.site.register(Category)
admin.site.register(GalleryImage)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'modal_title', 'process_title')
    search_fields = ('title', 'description', 'modal_title', 'process_title')
    list_filter = ('modal_subtitle',)
    fieldsets = (
        ('General', {
            'fields': ('title', 'icon', 'description')
        }),
        ('Modal', {
            'fields': ('modal_image', 'modal_subtitle', 'modal_title', 'modal_content')
        }),
        ('Proceso', {
            'fields': ('process_title', 'process_description', 'process_steps')
        }),
        ('Adicional', {
            'fields': ('additional_info',)
        }),
    )
    ordering = ('id',)