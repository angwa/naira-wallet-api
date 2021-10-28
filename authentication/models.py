from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        db_table = 'users'
    username = None
    email = models.CharField(max_length=200,unique=True)
    address = models.TextField(max_length=1000, null=True)
    email_verified = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    role_id = models.CharField(max_length=11, null = True)
    phone = models.CharField(max_length=11, null = True)
    bvn = models.CharField(max_length=10, null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']


class OTP(models.Model):
    class Meta:
        db_table = 'otps'
    user_id = models.CharField(max_length=11)
    purpose = models.CharField(max_length=30,default="email_verification")
    otp = models.IntegerField(unique=True)
    data = models.CharField(max_length=100, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
