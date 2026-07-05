from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Doctor
from .serializer import DoctorSerializer

# Create your views here.
class DoctorListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        patients = Doctor.objects.filter(
            created_by=request.user
        )

        serializer = DoctorSerializer(
            patients,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


    def post(self, request):

        serializer = DoctorSerializer(
            data=request.data
        )

        if serializer.is_valid():

            patient = serializer.save(
                created_by=request.user
            )

            return Response(
                DoctorSerializer(patient).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        patient = get_object_or_404(
            Doctor,
            id=id,
            created_by=request.user
        )

        serializer = DoctorSerializer(
            patient
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


    def put(self, request, id):

        patient = get_object_or_404(
            Doctor,
            id=id,
            created_by=request.user
        )

        serializer = DoctorSerializer(
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


    def delete(self, request, id):

        patient = get_object_or_404(
            Doctor,
            id=id,
            created_by=request.user
        )

        patient.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )