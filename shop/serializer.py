from rest_framework import serializers
from .models import Shop, Street, City


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = ('name',)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name',)


class CityAddressSerializer(serializers.ModelSerializer):
    address_rel = AddressSerializer(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'address_rel')


class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = AddressSerializer()

    class Meta:
        model = Shop
        fields = ('name', 'city', 'street', 'home', 'opening_time', 'closing_time')
