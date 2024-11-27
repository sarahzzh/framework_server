from django.db import models

# Create your models here.

#member
class Member(models.Model):
    member_id = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    alamat =models.CharField(max_length=200)
    email = models.EmailField()
    nohp = models.IntegerField()
    tgl_join = models.DateField()
    
class Trainer(models.Model):
    trainer_id = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    alamat =models.CharField(max_length=200)
    email = models.EmailField()
    nohp = models.IntegerField()
    tgl_join = models.DateField()

class Paket(models.Model):
    paket_id = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    durasi = models.CharField(max_length=50)
    harga = models.IntegerField()

class Transaksi(models.Model):
    transaksi_id = models.CharField(max_length=100) 
    member_id = models.CharField(max_length=100)
    trainer_id = models.CharField(max_length=100)
    tgl_transaksi = models.DateField()
    total = models.IntegerField()
