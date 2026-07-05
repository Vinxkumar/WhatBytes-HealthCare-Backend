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

        doctor = Doctor.objects.filter(
            created_by=request.user
        )

        serializer = DoctorSerializer(
            doctor,
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

            doctor = serializer.save(
                created_by=request.user
            )

            return Response(
                DoctorSerializer(doctor).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        doctor = get_object_or_404(
            Doctor,
            id=id,
            created_by=request.user
        )

        serializer = DoctorSerializer(
            doctor
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


    def put(self, request, id):

        doctor = get_object_or_404(
            Doctor,
            id=id,
            created_by=request.user
        )

        serializer = DoctorSerializer(
            doctor,
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

        doctor = get_object_or_404(
            Doctor,
            id=id,
            created_by=request.user
        )

        doctor.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )