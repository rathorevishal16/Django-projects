from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    file=models.FileField(upload_to='files/')
    
class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)