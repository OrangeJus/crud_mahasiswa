from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nama = models.CharField(max_length=255)
    nim = models.CharField(max_length=10, unique=True)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=10)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
    email = models.EmailField()
    status_mahasiswa = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.nama
    class Meta:
        ordering = ['created']