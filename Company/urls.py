from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyListCreateAPIView.as_view(), name='company_list_create'),
    path('<int:pk>/', views.CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company_detail'),

]