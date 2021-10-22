from django.shortcuts import render
from rest_framework import generics, permissions, serializers, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from authentication.models import User
from .serializer import UserRegistrationSerializer,UserProfileSerializer
from wallet.serializer import WalletSerializer
from rest_framework.response import Response


class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # #Create User wallet on registation
        wallet = WalletSerializer(data=request.data)
        wallet.is_valid()
   
        signedUser = User.objects.get(id=serializer.data['id'])
        wallet.save(user=signedUser)
    
        return Response({
            "message":"Registation successful",
            "data": {"user":serializer.data, "wallet":wallet.data},   
        }, status=status.HTTP_201_CREATED)
class ProfileApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        response = {
            "status":status.HTTP_200_OK,
            "message":"User profile retrieved successfully",
            "data":serializer.data,
        }
        return Response(response)