from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        
        fields = [
            "name",
            "email",
            "phone",
            "specialization",
            "created_at",
            "last_update"
        ]
        
        read_only_fields = [
            "id",
            "created_at",
            "last_update",
        ]
        
        