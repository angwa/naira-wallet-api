from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from authentication.models import User

class Wallet(models.Model):
    class Meta:
        db_table = 'wallets'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=30, decimal_places=2, default=0.00)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now_add=True)
    freezed_at =  models.DateTimeField(null=True)