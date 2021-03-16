from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import RoomViewSet, DormitoryViewSet

router = SimpleRouter()

router.register(r'room', RoomViewSet)
router.register(r'dormitory', DormitoryViewSet)

urlpatterns = router.urls

