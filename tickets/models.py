from django.db import models

# Create your models here.

#Guest --- Movie ---Reservation

class Movie(models.Model):
    hall=models,models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    date = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

class Reservation(models.Model):
    guest = models.ForeignKey(Guest , related_name='reservation',on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie , related_name='reservation',on_delete=models.CASCADE)