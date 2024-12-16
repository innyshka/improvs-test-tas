from django.contrib.auth.models import User
from rest_framework import serializers

from apps.user.utils.func import custom_to_representation


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'password',
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        return custom_to_representation(instance)

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)