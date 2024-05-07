from django.shortcuts import render
from .models import SliderItem


def index(request):
    items = SliderItem.objects.all()
    template = 'base.html'
    context = {
        'items': items,
    }
    return render(request, template, context)
