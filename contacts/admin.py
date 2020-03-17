from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'item', 'email', 'contact_date']
    list_display_links = ['id', 'name']
    list_per_page = 25
    search_fields = ['name', 'email', 'item']

