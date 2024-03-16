from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Tracking
from .serializers import TrackingSerializer


class TrackingListCreateAPIView(ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    

class TrackingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    

