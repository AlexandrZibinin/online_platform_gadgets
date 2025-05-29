from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsActiveUserPermission


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        permission_classes = [IsAuthenticated, IsActiveUserPermission]
