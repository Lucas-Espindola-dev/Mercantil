from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand)
    price = models.DecimalField()
    description = models.CharField(max_length=255)
    volume = models.FloatField()
    volume_metric = models.CharField(max_length=50)

