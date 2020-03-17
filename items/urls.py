from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='items'),
    path('<int:item_id>', views.item, name='item'),
    path('search', views.search, name='search')
]