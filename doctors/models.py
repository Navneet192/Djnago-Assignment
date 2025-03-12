from django.db import models
from django.conf import settings

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    experience = models.IntegerField(default=0)
    phone = models.CharField(max_length=15 , blank=True, null=True)

    def __str__(self):
        return self.name