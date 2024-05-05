from rest_framework import serializers
from .models import LapanganFutsal, Pemesanan

class LapanganFutsalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LapanganFutsal
        fields = '__all__'

class PemesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemesanan
        fields = '__all__'