from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Appointment
from .serializer import AppointmentSerializer


class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # POST /api/mappings/
    def post(self, request):
        serializer = AppointmentSerializer(
            data=request.data
        )

        if serializer.is_valid():
            patient = serializer.validated_data["patient"]

            # Security: user can only assign doctors
            # to patients they created
            if patient.created_by != request.user:
                return Response(
                    {
                        "message": "You cannot assign a doctor to this patient."
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

            appointment = serializer.save()

            return Response(
                AppointmentSerializer(appointment).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # GET /api/mappings/
    def get(self, request):
        mappings = Appointment.objects.all()

        serializer = AppointmentSerializer(
            mappings,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class PatientMappingView(APIView):
    permission_classes = [IsAuthenticated]

    # GET /api/mappings/<patient_id>/
    def get(self, request, id):
        mappings = Appointment.objects.filter(
            patient_id=id
        )

        serializer = AppointmentSerializer(
            mappings,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class MappingDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    # DELETE /api/mappings/<id>/
    def delete(self, request, id):
        mapping = get_object_or_404(
            Appointment,
            id=id
        )

        mapping.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )