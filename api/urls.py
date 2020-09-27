from django.urls import path, include
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
# register viewsets of api app here


urlpatterns = [
    path('', include(router.urls)),
]