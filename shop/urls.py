from django.urls import path
from . import views
from .models import Shop
from .serializer import ShopSerializer


urlpatterns = [
    path('GET/city/', views.CityList.as_view()),
    path('GET/city/<int:pk>/', views.CityDetail.as_view()),
    path('GET/city/<int:pk>/street/', views.CityDetailStreet.as_view()),
    path('POST/shop/', views.ShopViewCreate.as_view(queryset=Shop.objects.all(), serializer_class=ShopSerializer)),
    path('GET/shop/', views.ShopListView.as_view())
]
