from django.db import models

# Create your models here.
class Product(models.Model):
    maker = models.CharField("Maker", max_length=255)
    model = models.CharField("Model", max_length=255)
    type = models.CharField("Type", max_length=255)

    def __str__(self):
        return self.maker


class PC(models.Model):
    code = models.IntegerField("Code")
    model = models.CharField("Model", max_length=255)
    speed = models.IntegerField("Speed")
    ram = models.IntegerField("Ram")
    hd = models.IntegerField("HD")
    cd = models.CharField("CD", max_length=255)
    price = models.IntegerField("Price", null=True, blank=True)

    def __str__(self):
        return f"{self.model} - {self.speed} - {self.hd}"


class Laptop(models.Model):
    code = models.IntegerField("Code")
    model = models.CharField("Model", max_length=255)
    speed = models.IntegerField("Speed")
    ram = models.IntegerField("Ram")
    hd = models.IntegerField("HD")
    price = models.IntegerField("Price", null=True, blank=True)
    screen = models.IntegerField("Screen")

    def __str__(self):
        return self.model


class Printer(models.Model):
    code = models.IntegerField("Code")
    model = models.CharField("Model", max_length=255)
    color = models.CharField("Color", max_length=255, null=True)
    type = models.CharField("Type", max_length=255)
    price = models.IntegerField("Price", null=True, blank=True)

    def __str__(self):
        return self.model
