from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Company
from .serializers import CompanySerializer
from rest_framework import permissions

class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

