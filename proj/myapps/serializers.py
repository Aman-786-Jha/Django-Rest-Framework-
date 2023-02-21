from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Artist, Work, Client 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ClientSerializer(serializers.ModelSerializer):
    user_instance = UserSerializer()
    class Meta:
        model = Client
        fields = ['name', 'user_instance']

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['link', 'work_type']

class ArtistSerializer(serializers.ModelSerializer):
    work = WorkSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['name', 'work']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],password=validated_data['password'])
                                        
        return user