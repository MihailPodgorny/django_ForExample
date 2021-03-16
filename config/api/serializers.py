from rest_framework.serializers import ModelSerializer

from .models import Room, Dormitory


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number', 'floor', 'number_of_beds')


class DormitorySerializer(ModelSerializer):
    class Meta:
        model = Dormitory
        fields = ('id', 'number', 'faculty', 'number_of_floors', 'number_of_rooms')
