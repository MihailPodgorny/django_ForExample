from django.test import TestCase

from ..models import Room, Dormitory
from ..serializers import RoomSerializer, DormitorySerializer


class RoomDormitorySerializerTestCase(TestCase):
    def setUp(self):
        self.dormitory_1 = Dormitory.objects.create(number=5, faculty='ЭТФ', number_of_floors=9)
        self.dormitory_2 = Dormitory.objects.create(number=3, faculty='ЭМФ', number_of_floors=4, number_of_rooms=80)
        self.room_1 = Room.objects.create(number=301, floor=3, dormitory=self.dormitory_1)
        self.room_2 = Room.objects.create(number=203, floor=2, dormitory=self.dormitory_1, number_of_beds=2)

    def test_room_data(self):
        serializer_data = RoomSerializer([self.room_1, self.room_2], many=True).data
        expected_data = [
            {
                'id': self.room_1.id,
                'number': 301,
                'floor': 3,
                'number_of_beds': 4
            },
            {
                'id': self.room_2.id,
                'number': 203,
                'floor': 2,
                'number_of_beds': 2
            },
        ]
        self.assertEqual(serializer_data, expected_data)

    def test_dormitory_data(self):
        serializer_data = DormitorySerializer([self.dormitory_1, self.dormitory_2], many=True).data
        expected_data = [
            {
                'id': self.dormitory_1.id,
                'number': 5,
                'faculty': 'ЭТФ',
                'number_of_floors': 9,
                'number_of_rooms': 100
            },
            {
                'id': self.dormitory_2.id,
                'number': 3,
                'faculty': 'ЭМФ',
                'number_of_floors': 4,
                'number_of_rooms': 80
            },
        ]
        self.assertEqual(serializer_data, expected_data)
