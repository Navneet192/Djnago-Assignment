from django.db import models
from django.conf import settings

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patients")  
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default='Other')
    address = models.TextField(default="Unknown")
    phone = models.CharField(max_length=15 , default='0000000000')

    def __str__(self):
        return self.name