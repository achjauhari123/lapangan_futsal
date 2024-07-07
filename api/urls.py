from django.urls import path
from .views import LapanganFutsalListCreateAPIView, LapanganFutsalDetailAPIView, PemesananListCreateAPIView, PemesananDetailAPIView

urlpatterns = [
    path('lapangan-futsal/', LapanganFutsalListCreateAPIView.as_view(), name='lapanganfutsal-list-create'),
    path('lapangan-futsal/<int:pk>/', LapanganFutsalDetailAPIView.as_view(), name='lapanganfutsal-detail'),
    path('pemesanan/', PemesananListCreateAPIView.as_view(), name='pemesanan-list-create'),
    path('pemesanan/<int:pk>/', PemesananDetailAPIView.as_view(), name='pemesanan-detail'),
]
