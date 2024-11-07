from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import update_last_login

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'created_at', 'updated_at', 'is_active']
    
    

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(user=self.user)
        user  = CustomUserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = user
        
        update_last_login(None, self.user)
        return data
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def create(self, attrs):
    #     data = super().create(attrs)
    #     refresh = self.get_token(user=self.user)
    #     user = CustomUserSerializer(self.user).data
    #     data['refresh'] = str(refresh)
    #     data['access'] = str(refresh.access_token)
    #     data['user'] = user
        
    #     update_last_login(None, self.user)
    #     return data
        
        