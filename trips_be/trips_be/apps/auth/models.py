from django.conf import settings
from django.db import models

class TourGuide(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    identification = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=150)
    telephone = models.IntegerField()