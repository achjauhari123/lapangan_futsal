from django.db import models

# Create your models here.
class LapanganFutsal(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    harga_per_jam = models.DecimalField(max_digits=10, decimal_places=2)
    kapasitas_maksimum = models.IntegerField()

    def __str__(self):
        return self.nama

class Pemesanan(models.Model):
    lapangan = models.ForeignKey(LapanganFutsal, on_delete=models.CASCADE)
    waktu_mulai = models.DateTimeField()
    durasi_jam = models.IntegerField()
    nama_pelanggan = models.CharField(max_length=100)
    telepon_pelanggan = models.CharField(max_length=15)
    status_pembayaran = models.BooleanField(default=False)  # False untuk belum dibayar, True untuk sudah dibayar
    status_pemesanan = models.CharField(max_length=20, default='pending')  # pending, sedang berjalan, selesai, dibatalkan

    def __str__(self):
        return f"Pemesanan untuk {self.lapangan.nama} pada {self.waktu_mulai}"
