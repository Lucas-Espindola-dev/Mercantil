from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="product_brand")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=255)
    volume = models.FloatField()
    volume_metric = models.CharField(max_length=50)
    bars_code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

