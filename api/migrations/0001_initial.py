# Generated by Django 5.0.4 on 2024-05-05 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LapanganFutsal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('harga_per_jam', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kapasitas_maksimum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pemesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_mulai', models.DateTimeField()),
                ('durasi_jam', models.IntegerField()),
                ('nama_pelanggan', models.CharField(max_length=100)),
                ('telepon_pelanggan', models.CharField(max_length=15)),
                ('status_pembayaran', models.BooleanField(default=False)),
                ('status_pemesanan', models.CharField(default='pending', max_length=20)),
                ('lapangan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lapanganfutsal')),
            ],
        ),
    ]
