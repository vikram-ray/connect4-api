from django.urls import path, include
from rest_framework import routers

from .views import Connect4ViewSet

router = routers.DefaultRouter()
# register viewsets of api app here

router.register("", Connect4ViewSet, basename="connect")

urlpatterns = [
    path('', include(router.urls)),
]

