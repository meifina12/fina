from django.db import models

# Create your models here.


class Hewan(models.Model):
    Hewan = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Hewan}"


class Jenis_Hewan(models.Model):
    Hewan = models.ForeignKey(Hewan, on_delete=models.CASCADE)
    Jenis_Hewan = models.CharField(max_length=100)
    Makanan_Hewan = models.TextField()

    def __str__(self):
        return f"{self.Jenis_Hewan} {self.Makanan_Hewan}"