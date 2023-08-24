from django.db import models

# Create your models here.

class Car(models.Model):
    GEAR=(
        ('a', 'automatic'),
        ('m', 'manual'),
    )
    plate_number=models.CharField(max_length=20,unique=True)
    brand=models.CharField(max_length=30)
    model=models.CharField(max_length=20)
    year=models.SmallIntegerField()
    gear=models.CharField(max_length=1,choices=GEAR)
    rent_per_day=models.DecimalField(max_digits=8, decimal_places=3)
    availability=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.brand}-{self.model}-{self.plate_number}"