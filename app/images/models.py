from django.db import models
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    title = models.CharField(max_length=100)
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return self.title
