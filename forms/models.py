import email
from tempfile import NamedTemporaryFile
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.Name
    
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
class Booking(models.Model):
    Name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    contact = models.CharField(max_length=12)
    booking_date = models.DateField()
    booking_place = models.TextField()
    adult =models.TextField(max_length=10)
    children =models.TextField(max_length=10)
    def __str__(self):
        return self.Name