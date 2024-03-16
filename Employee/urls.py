from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListCreateAPIView.as_view(), name='employee_list_create'),
    path('<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee_detail'),

]