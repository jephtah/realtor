from django.contrib import admin

from .models import Item


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    search_fields = ('id', 'price', 'title')
    list_per_page = 25
    list_editable = ('is_published',)


admin.site.register(Item, ListingAdmin)
