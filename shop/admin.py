from django.contrib import admin
from .models import Address, Shop, City


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'address']
    list_filter = ['name', 'city', 'address']
    search_fields = ['name', 'city', 'address']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Address)
admin.site.register(City)
