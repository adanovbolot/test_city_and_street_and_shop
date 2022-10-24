from django.urls import path
from . import views
from rest_framework import routers


urlpatterns = [
    path('GET/city/', views.CityList.as_view()),
    path('GET/city/<int:pk>/', views.CityDetail.as_view()),
    path('GET/city/<int:pk>/street/', views.CityDetailStreet.as_view()),
]
