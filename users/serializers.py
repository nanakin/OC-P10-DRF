from rest_framework import serializers
from .models import User
from datetime import date

REQUIRED_AGE = 15


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "birth_date", "created_time", "can_be_contacted", "can_data_be_shared"]

    def validate_birth_date(self, birth_date):
        if date(year=(birth_date.year + REQUIRED_AGE), month=birth_date.month, day=birth_date.day) \
                > date.today():
            raise serializers.ValidationError('Too young')
        return birth_date


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "created_time", "can_be_contacted", "can_data_be_shared"]