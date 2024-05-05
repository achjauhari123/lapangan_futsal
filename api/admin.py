from django.contrib import admin
from .models import LapanganFutsal, Pemesanan

class LapanganFutsalAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga_per_jam', 'kapasitas_maksimum')
    search_fields = ('nama',)

class PemesananAdmin(admin.ModelAdmin):
    list_display = ('lapangan', 'waktu_mulai', 'durasi_jam', 'nama_pelanggan', 'status_pembayaran', 'status_pemesanan')
    list_filter = ('status_pembayaran', 'status_pemesanan')
    search_fields = ('lapangan__nama', 'nama_pelanggan', 'telepon_pelanggan')
    date_hierarchy = 'waktu_mulai'

admin.site.register(LapanganFutsal, LapanganFutsalAdmin)
admin.site.register(Pemesanan, PemesananAdmin)
