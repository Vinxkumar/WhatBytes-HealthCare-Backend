from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth import authenticate


from .serializers import (
    SignupSerializer,
    LoginSerializer
)

class SignUpView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SignupSerializer(data = request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User Created Sucessfully",
                    "user": SignupSerializer(user).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(
            data=request.data
        )
        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_404_NOT_FOUND
            )
        
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        
        user = authenticate(
            request=request,
            email = email,
            password=password
        )
        
        if user is None:
            return Response(
                {
                    "message" : "Invalid Credentials"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        token = AccessToken.for_user(user)
        
        return Response(
            {
                "message":"Login Successfull",
                "token": str(token),
                "user": {
                    "name": user.name,
                    "email": user.email
                }
            },
            status=status.HTTP_200_OK
        )
