from django.db import models

# Create your models here.

# class Flight:
# Source
# Destination
# tickets 
# Airline
# Date

class Flight(models.Model):
    # created 
    # updated
    source = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    airline = models.CharField(max_length=100, null=False)
    tickets = models.IntegerField(default=0)    
    date = models.DateTimeField(null=False)
    image = models.ImageField(upload_to="plane_images", default="shark.jpg")

    def __str__(self):
        return f"{self.source} - {self.destination} - {self.date}"