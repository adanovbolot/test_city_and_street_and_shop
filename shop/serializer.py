from rest_framework import serializers
from .models import Shop, Address, City


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name',)


class CityAddressSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = City
        fields = "__all__"
