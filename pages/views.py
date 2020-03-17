from django.shortcuts import render

from items.choices import price_choices, bedroom_choices, state_choices
from items.models import Item
from realtors.models import Realtor


def index(request):
    items = Item.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'items': items,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,

    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
