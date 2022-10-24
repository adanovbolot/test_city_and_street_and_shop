from django.contrib import admin
from .models import Address, Shop, City, CityAndStreet


class CityAndStreetInline(admin.TabularInline):
    model = CityAndStreet
    extra = 0


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'address']
    list_filter = ['name', 'city', 'address']
    search_fields = ['name', 'city', 'address']


class CityAdmin(admin.ModelAdmin):
    inlines = [CityAndStreetInline]


admin.site.register(Shop, ShopAdmin)
admin.site.register(Address)
admin.site.register(City, CityAdmin)
