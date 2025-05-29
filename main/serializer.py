from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from main.models import Agent, Product, Link
from users.permissions import IsActiveUserPermission


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = "__all__"
        read_only_fields = ("level",)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = (
            "created_at",
            "duty",
        )
