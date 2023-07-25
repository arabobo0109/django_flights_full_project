from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Flight:
# Source
# Destination
# tickets 
# Airline
# Date


# User:
#  User_ID (PK)
#  Name
#  Password
#  RegistraƟon date

# Soundlist:
#  Playlist_ID (PK)
#  Playlist Name
#  User_ID (FK) 

from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    city = models.CharField(max_length=100, null=True)
    

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=100, null=False)


# class SoundList(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Sound(models.Model):
#     name = models.CharField(max_length=100, null=False)
#     sound_list = models.ManyToManyField(SoundList)

    

class Flight(models.Model):
    # created 
    # updated
    source = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    airline = models.CharField(max_length=100, null=False)
    tickets = models.IntegerField(default=0)    
    date = models.DateTimeField(null=False)
    image = models.ImageField(upload_to="plane_images", default="/plane_images/shark.jpg")

    def __str__(self):
        return f"{self.source} - {self.destination} - {self.date}"