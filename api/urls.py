from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LapanganFutsalViewSet, PemesananViewSet

router = DefaultRouter()
router.register(r'lapangan-futsal', LapanganFutsalViewSet)
router.register(r'pemesanan', PemesananViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
