from django.db import models
from django.contrib.auth.models import User
import time
import os


class Mahasiswa(models.Model):
    nim = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    PRIA = 'PR'
    WANITA = 'WN'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),

    )
    jenis_kelamin = models.CharField(
        max_length=2,
        choices=JK_CHOICES,
        default=PRIA,
    )
    born_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    def __str__(self):
        return self.nim

    class Meta:
        db_table = 'mahasiswa'
        ordering = ['id']


class MataPerkuliahan(models.Model):
    name = models.CharField(max_length=100)
    amount_sks = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mataperkuliahan'
        ordering = ['id']

