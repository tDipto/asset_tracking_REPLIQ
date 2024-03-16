from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceListCreateAPIView.as_view(), name='device_list_create'),
    path('<int:pk>/', views.DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device_detail'),

]