from rest_framework import serializers
from .models import Bank

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id','account_name','account_type','bank_name','account_number','created_at')
