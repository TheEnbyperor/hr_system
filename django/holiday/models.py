from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Holiday(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='holiday')
    start = models.DateTimeField()
    end = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee.first_name}: {self.start} - {self.end}"
