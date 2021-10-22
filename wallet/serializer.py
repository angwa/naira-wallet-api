from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id','amount','created_at','updated_at','freezed_at')
        extra_kwargs = {'freezed_at':{'write_only':True}}
    

    