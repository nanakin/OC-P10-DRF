from rest_framework import serializers
from .models import User
from datetime import date
from django.contrib.auth import password_validation

REQUIRED_AGE = 15


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "birth_date", "can_be_contacted", "can_data_be_shared", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_birth_date(self, birth_date):
        if date(year=(birth_date.year + REQUIRED_AGE), month=birth_date.month, day=birth_date.day) > date.today():
            raise serializers.ValidationError('Too young')
        return birth_date

    def validate_password(self, value):
        password_validation.validate_password(value)  # raise a validation Error
        return value


class UserCreateSerializer(UserSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserListSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["id", "username"]


class UserDetailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["username", "can_be_contacted", "can_data_be_shared", "created_time", "birth_date"]


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password'))
        instance.save()
        return instance

    def validate_password(self, value):
        password_validation.validate_password(value)  # raise a validation Error
        return value
