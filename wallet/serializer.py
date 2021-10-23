from django.db import models
from rest_framework import serializers
from .models import Wallet
from authentication. models import User

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id','amount','created_at','updated_at','freezed_at')
        extra_kwargs = {'freezed_at':{'write_only':True}}
    

    
class ShowWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet 
        fields = ('amount','freezed_at')