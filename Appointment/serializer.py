from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Appointment
        
        fields = [
            "id",
            "patient",
            "doctor",
            "note",
            "created_at"
        ]
        read_only_field = [
            "id",
            "created_at",
            
        ]