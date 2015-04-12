from rest_framework import serializers
from django.contrib.auth.models import User


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
