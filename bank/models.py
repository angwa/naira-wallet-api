from django.db import models
from authentication.models import User

class Bank(models.Model):
    class Meta:
        db_table = 'banks'
    account_type = models.CharField(max_length=100, null=False)
    bank_name = models.CharField(max_length=100, null=False)
    account_name = models.CharField(max_length=100, null=False)
    account_number = models.CharField(max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)