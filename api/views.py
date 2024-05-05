from rest_framework import viewsets
from .models import LapanganFutsal, Pemesanan
from .serializers import LapanganFutsalSerializer, PemesananSerializer

class LapanganFutsalViewSet(viewsets.ModelViewSet):
    queryset = LapanganFutsal.objects.all()
    serializer_class = LapanganFutsalSerializer

class PemesananViewSet(viewsets.ModelViewSet):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSerializer
