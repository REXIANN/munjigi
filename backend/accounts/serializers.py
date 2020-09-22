from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth import authenticate


# 회원가입

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'password', 'name', 'birth')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], validated_data['nickname'], validated_data['password']
        )
        return user


# 접속중인 유저인지 확인
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('id', 'email')


# 로그인
class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to login with provided credentials.")


# 프로필
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')