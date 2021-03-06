from rest_framework import serializers
from .models import OTP, User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password')
        extra_kwargs = {
            "password":{"write_only":True},
            }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','first_name', 'last_name','address', 'phone','bvn','email_verified')

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ()