from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser) :
    username = None
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    # password = models.
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email