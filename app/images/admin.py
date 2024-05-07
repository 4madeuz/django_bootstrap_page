from django.contrib import admin
from .models import SliderItem
from filer.models import Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['title', 'image_tag',]
