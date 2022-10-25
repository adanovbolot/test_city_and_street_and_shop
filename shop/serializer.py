from rest_framework import serializers
from .models import Shop, Address, City


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name')


class CityAddressSerializer(serializers.ModelSerializer):
    address_rel = AddressSerializer(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'address_rel')


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'city', 'address', 'home', 'opening_time', 'closing_time')
