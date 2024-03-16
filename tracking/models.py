from django.db import models
from Device.models import Device
from Employee.models import Employee
from django.core.validators import MinValueValidator

class Tracking(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

    checkout_at = models.DateTimeField()
    returned_at = models.DateTimeField(blank=True,null=True)

    condition_checkout = models.TextField()
    condition_returned = models.TextField()

    total_number = models.IntegerField(default=1,validators=[MinValueValidator(1)])


    def __str__(self):
        return f"{self.device} {self.employee} {self.checkout_at} {self.returned_at}"
