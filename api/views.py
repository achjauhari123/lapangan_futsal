from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LapanganFutsal, Pemesanan
from .serializers import LapanganFutsalSerializer, PemesananSerializer

class LapanganFutsalListCreateAPIView(APIView):
    def get(self, request):
        lapangan = LapanganFutsal.objects.all()
        serializer = LapanganFutsalSerializer(lapangan, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LapanganFutsalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LapanganFutsalDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return LapanganFutsal.objects.get(pk=pk)
        except LapanganFutsal.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        lapangan = self.get_object(pk)
        serializer = LapanganFutsalSerializer(lapangan)
        return Response(serializer.data)
    
    def put(self, request, pk):
        lapangan = self.get_object(pk)
        serializer = LapanganFutsalSerializer(lapangan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        lapangan = self.get_object(pk)
        lapangan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PemesananListCreateAPIView(APIView):
    def get(self, request):
        pemesanan = Pemesanan.objects.all()
        serializer = PemesananSerializer(pemesanan, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PemesananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PemesananDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Pemesanan.objects.get(pk=pk)
        except Pemesanan.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pemesanan = self.get_object(pk)
        serializer = PemesananSerializer(pemesanan)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pemesanan = self.get_object(pk)
        serializer = PemesananSerializer(pemesanan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        pemesanan = self.get_object(pk)
        pemesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
