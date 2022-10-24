from rest_framework import serializers
from .models import Shop, Address, City, CityAndStreet


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name',)


class CityAddressSerializer(serializers.ModelSerializer):
    address_rel = AddressSerializer(many=True)

    class Meta:
        model = City
        fields = ('name',)
