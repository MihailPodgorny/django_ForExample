from xml.etree.ElementInclude import include

from django.urls import path

from .views import IndexView, vk_auth

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('auth/', vk_auth),
]
