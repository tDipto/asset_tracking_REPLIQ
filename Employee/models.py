from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser 

from Company.models import Company

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()


    def __str__(self):
        return f"{self.user} - {self.company} - {self.phone}"