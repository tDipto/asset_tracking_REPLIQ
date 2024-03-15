from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.address} - {self.phone_number}"
