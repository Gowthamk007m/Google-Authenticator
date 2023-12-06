from rest_framework import serializers
from django.contrib.auth.models import User

from allauth.socialaccount.models import SocialAccount


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'


class Google_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = '__all__'