from django.contrib import admin
from .models import SliderItem
from easy_thumbnails.files import get_thumbnailer
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            thumbnail_options = {'size': (100, 100), 'crop': True}
            thumbnail_url = get_thumbnailer(obj.image).get_thumbnail(thumbnail_options).url
            return format_html('<img src="{}"/>'.format(thumbnail_url))
        return format_html('<span>No Image</span>')

    image_tag.short_description = 'Image'
    list_display = ['title', 'image_tag']
