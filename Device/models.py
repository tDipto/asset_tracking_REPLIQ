from django.db import models
from Company.models import Company
from django.core.validators import MinValueValidator

class Device(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    specification = models.TextField()

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    total_number = models.IntegerField(default=0,validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} {self.company} ({self.total_number})"