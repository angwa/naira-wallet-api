
from django.db.models.base import Model
from django.shortcuts import render
from rest_framework import generics, permissions, serializers, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from authentication.models import OTP, User
from wallet.models import Wallet
from .serializer import UserRegistrationSerializer,UserProfileSerializer,OtpSerializer
from wallet.serializer import WalletSerializer, ShowWalletSerializer
from rest_framework.response import Response
from .sendsms.sms import SendSMS
from .verifybvn.bvn import Bvn
from .helpers.otpgenerator import Otp


class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #sending OTP for verification

        otp = OtpSerializer(data=request.data)
        otp.is_valid(raise_exception=True)
        otp.save(user_id=serializer.data['id'], otp=Otp.generateOTP())


        # #Create User wallet on registation
        wallet = WalletSerializer(data=request.data)
        wallet.is_valid()
   
        signedUser = User.objects.get(id=serializer.data['id'])
        wallet.save(user=signedUser)
    
        return Response({
            "message":"Registation successful",
            "data": {"user":serializer.data, "wallet":wallet.data},   
        }, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def post(self, request):
        otp = OTP.objects
        if not otp.filter(otp=request.data["otp"]).exists():
            return Response({
                "message":"OTP not valid or has been used."
            }, status=status.HTTP_400_BAD_REQUEST)

        data =  otp.get(otp=request.data["otp"])
        instance = User.objects.get(id=data.user_id)
        instance.email_verified = "1"
        instance.save()

        #deleting OTP from OTP table after been used
        data.delete()
        serializer = UserProfileSerializer(instance)

        
        return Response({
            "message":"Email verified successfully",
            "data":serializer.data
            })


class ProfileApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        wallet_id = Wallet.objects.get(user_id=request.user.id)
        wallet = ShowWalletSerializer(wallet_id)
     
        response = {
            "status":status.HTTP_200_OK,
            "message":"User profile retrieved successfully",
            "data":{"user":serializer.data, "wallet":wallet.data},
        }
        return Response(response)



class VerifyPhoneApi(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):

        #sending OTP for verification
        otp = OtpSerializer(data=request.data)
        otp.is_valid(raise_exception=True)
        otp.save(user_id=request.user.id, otp=Otp.generateOTP(), data=request.data["phone"])

        phone = SendSMS.send()

        return Response({phone})
    

    def put(self, request):
        otp = OTP.objects
        if not otp.filter(otp=request.data["otp"]).exists():
            return Response({
                "message":"OTP not valid or has been used."
            }, status=status.HTTP_400_BAD_REQUEST)

        data =  otp.get(otp=request.data["otp"])
        instance = User.objects.get(id=data.user_id)
        instance.phone = data.data
        instance.save()

        #deleting OTP from OTP table after been used
        data.delete()
        serializer = UserProfileSerializer(instance)

        
        return Response({
            "message":"Email verified successfully",
            "data":serializer.data
            })





class VerifyBvn(generics.GenericAPIView):
    def post(self, request):
        bvn = Bvn.verify("22278447875")

        return Response({bvn})