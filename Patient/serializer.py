from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient

        fields = [
            "id",
            "name",
            "age",
            "gender",
            "address",
            "phone",
            "created_at",
            "last_update",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "last_update",
        ]

    def validate_age(self, value):
        if value > 130:
            raise serializers.ValidationError(
                "Age cannot be greater than 130."
            )

        return value