from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrackingListCreateAPIView.as_view(), name='tracking_list_create'),
    path('<int:pk>/', views.TrackingRetrieveUpdateDestroyAPIView.as_view(), name='tracking_detail'),

]