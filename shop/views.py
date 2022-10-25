from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializer import CitySerializer, CityAddressSerializer, ShopSerializer
from .models import City, Shop
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def detail(self, request):
        queryset = self.get_queryset()
        serializer = CitySerializer(queryset)
        if Response.status_code == '400':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)


class CityList(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def list_obj(self, request):
        queryset = self.get_queryset()
        serializer = CitySerializer(queryset, many=True)
        if Response.status_code == '400':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)


class CityDetailStreet(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityAddressSerializer

    def detail(self, request):
        queryset = self.get_queryset()
        serializer = CityAddressSerializer(queryset)
        if Response.status_code == '400':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)


class ShopViewCreate(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_obj_id(self):
        queryset = Shop.objects.filter(id=self.request.id)
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)


class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_fields = ['name', 'city', 'street']
    search_fields = ['name', 'city', 'street']
    ordering_fields = ['name', 'city', 'street']

    def list_obj(self, request):
        queryset = self.get_queryset()
        serializer = CitySerializer(queryset, many=True)
        if Response.status_code == '400':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
