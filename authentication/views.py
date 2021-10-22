from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializer import UserRegistrationSerializer,UserProfileSerializer
from rest_framework.response import Response


class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message":"Registation successful",
            "data": serializer.data,
        }, status=status.HTTP_201_CREATED)
class ProfileApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        response = {
            "status":status.HTTP_200_OK,
            "message":"User profile retrieved successfully",
            "data":serializer.data
        }
        return Response(response)