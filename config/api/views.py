from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .serializers import RoomSerializer, DormitorySerializer
from .models import Room, Dormitory


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    # filter_fields = ['number']
    search_fields = ['number']
    ordering_fields = ['dormitory', 'number']
    permission_classes = [IsAuthenticatedOrReadOnly]


class DormitoryViewSet(ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filter_fields = ['number']
    search_fields = ['number']
    ordering_fields = ['number']
    permission_classes = [IsAuthenticatedOrReadOnly]
