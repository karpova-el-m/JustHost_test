from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VPSViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'vps', VPSViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
