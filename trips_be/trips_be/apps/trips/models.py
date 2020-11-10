from django.conf import settings
from django.db import models

class Trip(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    match = models.IntegerField()
    long_days = models.IntegerField()
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=True)
    likes = models.IntegerField()

class Booking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Like(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField()