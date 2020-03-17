from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from items.choices import price_choices, bedroom_choices, state_choices
from .models import Item


def index(request):
    items = Item.objects.order_by('-list_date').filter(is_published=True)

    # setting up pagination
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)

    context = {
        'items': paged_items
    }
    return render(request, 'items/items.html', context)


def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    context = {
        "item": item
    }
    return render(request, 'items/item.html', context)


def search(request):
    queryset_list = Item.objects.order_by('-list_date').filter(is_published=True)

    #Keywords searched for
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Keywords searched for
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Keywords searched for
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Keywords searched for
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Keywords searched for
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'items': queryset_list,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'values': request.GET

    }
    return render(request, 'items/search.html', context)
