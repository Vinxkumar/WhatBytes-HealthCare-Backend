from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Patient
from .serializer import PatientSerializer


class PatientListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # GET /api/patients/
    def get(self, request):

        patients = Patient.objects.filter(
            created_by=request.user
        )

        serializer = PatientSerializer(
            patients,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


    # POST /api/patients/
    def post(self, request):

        serializer = PatientSerializer(
            data=request.data
        )

        if serializer.is_valid():

            patient = serializer.save(
                created_by=request.user
            )

            return Response(
                PatientSerializer(patient).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PatientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # GET /api/patients/<id>/
    def get(self, request, id):

        patient = get_object_or_404(
            Patient,
            id=id,
            created_by=request.user
        )

        serializer = PatientSerializer(
            patient
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


    # PUT /api/patients/<id>/
    def put(self, request, id):

        patient = get_object_or_404(
            Patient,
            id=id,
            created_by=request.user
        )

        serializer = PatientSerializer(
            patient,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # DELETE /api/patients/<id>/
    def delete(self, request, id):

        patient = get_object_or_404(
            Patient,
            id=id,
            created_by=request.user
        )

        patient.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )