from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Posts,Profile
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields='__all__'





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #fields = ['user','first_name','last_name','email','city','board','grade','id']
        fields='__all__'