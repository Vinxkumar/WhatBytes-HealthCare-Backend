from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    
    
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female")
    ]
    
    name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )
    address = models.TextField(max_length=255)
    phone = models.CharField(max_length=13, unique=True)
    
    # medical_history
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patients"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name