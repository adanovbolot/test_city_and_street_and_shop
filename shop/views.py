from .serializer import CitySerializer, CityAddressSerializer
from .models import City
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminUser]

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
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CitySerializer(queryset, many=True)
        if Response.status_code == '400':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)


class CityDetailStreet(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminUser]

    def detail(self, request):
        queryset = self.get_queryset()
        serializer = CityAddressSerializer(queryset)
        if Response.status_code == '400':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
