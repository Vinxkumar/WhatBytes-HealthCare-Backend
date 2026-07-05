from django.db import models
from django.conf import settings

from django.db import connection

print(connection.settings_dict["ENGINE"])
print(connection.settings_dict["NAME"])


   
class Doctor(models.Model):
    
    SPELIZATION_CARDIO = "C"
    SPELIZATION_ENT = "E"
    
    SPELIZATION_CHOICES = [
        (SPELIZATION_CARDIO, "Cardiologist"),
        (SPELIZATION_ENT, "ENT"),
        
    ]
    
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    
    specialization = models.CharField(
        max_length= 1,
        choices=SPELIZATION_CHOICES
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctors"

    )
       
    def __str__(self):
        return self.name