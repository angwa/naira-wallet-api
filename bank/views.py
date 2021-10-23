from django.shortcuts import render
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from authentication.models import User
from .serializer import BankSerializer
from rest_framework.response import Response
from .models import Bank as BankModel
from rest_framework import permissions, serializers, status, generics

class Bank(generics.GenericAPIView):
    permission_class = [permissions.IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication
    def post(self, request):
        serializer = BankSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        signedUser = User.objects.get(id=request.user.id)
        serializer.save(user=signedUser)
        response = {
            "message":"New bank created successfully",
            "data":serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)
    def get(self, request):
        banks = BankModel.objects.filter(user_id=request.user.id)
        serializer = BankSerializer(banks, many=True)
        
        response = {
            "status": status.HTTP_200_OK,
            "message":"Banks Retrieved successfully",
            "data":serializer.data
        }
        return Response(response)