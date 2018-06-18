from django.db import models

class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ForiegnKeyUser(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='students',
        blank=True,
        null=True,
    )