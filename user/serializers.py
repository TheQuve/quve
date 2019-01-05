from typing import Dict, Any

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):

    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'tags',
        )


class SignUpSerializer(RegisterSerializer):

    cleaned_data: Dict[str, Any]

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user
