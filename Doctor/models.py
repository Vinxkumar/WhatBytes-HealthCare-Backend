from django.db import models

# Create your models here.
class Specialization(models.TextChoices):
    CARDIO = "C", "Cardiologist",
    ENT = "E", "ENT"
    
class Doctor(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    
    specialization = models.CharField(
        max_length= 1,
        choices=Specialization.choices
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    # created_by