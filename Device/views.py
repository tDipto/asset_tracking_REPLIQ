from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Device
from .serializers import DeviceSerializer


class DeviceListCreateAPIView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    

class DeviceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    

