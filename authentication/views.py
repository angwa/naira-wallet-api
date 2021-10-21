from django.shortcuts import render
from rest_framework import generics
from .serializer import UserRegistrationSerializer
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
        })