from django.db import models


class Gender(models.TextChoices):
    MALE = 'M', "Male",
    FEMALE = "FM", "Female"

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )
    address = models.TextField(max_length=255)
    phone = models.CharField(max_length=13)
    
    # medical_history
    # created_by
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)