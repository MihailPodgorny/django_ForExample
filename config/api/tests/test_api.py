from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Room, Dormitory
from ..serializers import RoomSerializer, DormitorySerializer


class RoomAPITestCase(APITestCase):
    def setUp(self):
        self.dormitory_1 = Dormitory.objects.create(number=5, faculty='ЭТФ', number_of_floors=9)
        self.room_1 = Room.objects.create(number=301, floor=3, dormitory=self.dormitory_1)
        self.room_2 = Room.objects.create(number=203, floor=2, dormitory=self.dormitory_1)

    def test_room_get(self):
        url_list = reverse('room-list')
        # url_detail = reverse('room-detail')
        response = self.client.get(url_list)
        serializer_data = RoomSerializer([self.room_1, self.room_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_room_get_search(self):
        url_list = reverse('room-list')
        response = self.client.get(url_list, data={'search': '301'})
        serializer_data = RoomSerializer([self.room_1], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)


class DormitoryAPITestCase(APITestCase):
    def setUp(self):
        self.dormitory_1 = Dormitory.objects.create(number=5, faculty='ЭТФ', number_of_floors=9)
        self.dormitory_2 = Dormitory.objects.create(number=3, faculty='ЭМФ', number_of_floors=4, number_of_rooms=80)

    def test_dormitory_get(self):
        url_list = reverse('dormitory-list')
        response = self.client.get(url_list)
        serializer_data = DormitorySerializer([self.dormitory_1, self.dormitory_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)
