from django.contrib import admin
from .models import Street, Shop, City


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'street']
    list_filter = ['name', 'city', 'street']
    search_fields = ['name', 'city', 'street']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Street)
admin.site.register(City)
