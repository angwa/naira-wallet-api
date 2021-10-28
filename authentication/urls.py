from os import name
from django.urls import path
from . import views 
from rest_framework_simplejwt import views as jwt_views

urlpatterns  = [
    path('profile', views.ProfileApi.as_view(), name='profile'),
    path('register', views.RegisterAPI.as_view(), name='user_registration'),
    path('verify-email', views.VerifyEmail.as_view(), name ='verifyemail'),
    path('login', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('verify-phone', views.VerifyPhoneApi.as_view(), name ='request_phone_otp'),
    path('verify-bvn', views.VerifyBvn.as_view(), name ='verifybvn'),
  
]