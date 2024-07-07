from django.db import models
from api.models import LapanganFutsal  # Mengimpor model dari aplikasi 'lapangan'

class Review(models.Model):
    lapangan = models.ForeignKey(LapanganFutsal, on_delete=models.CASCADE)
    rating = models.IntegerField()
    komentar = models.TextField(blank=True, null=True)
    tanggal_review = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review untuk {self.lapangan.nama} - Rating: {self.rating}"
