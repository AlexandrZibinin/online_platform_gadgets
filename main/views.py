from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    get_object_or_404,
)

from main.models import Agent, Product, Link
from main.serializer import AgentSerializer, ProductSerializer, LinkSerializer


class AgentCreateAPIView(generics.CreateAPIView):
    serializer_class = AgentSerializer

    def perform_create(self, serializer):
        """уровень завода всегда находится на уровне 0"""
        agent = serializer.save()
        if agent.type_agent == "Завод":
            agent.level = 0
        agent.save()


class AgentListAPIView(generics.ListAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


class AgentRetrieveAPIView(RetrieveAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class AgentUpdateAPIView(UpdateAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class AgentDestroyAPIView(DestroyAPIView):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        """при создании сделки уровень покупателя меняется в зависимости от уровня продавца"""
        link = serializer.save()
        buyer = get_object_or_404(Agent, id=link.buyer.id)
        if link.supplier != link.buyer:
            link.buyer.level = link.supplier.level + 1
        else:
            link.buyer.level = 1
        buyer.level = link.buyer.level
        buyer.save()
        link.save()


class LinkListAPIView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class LinkRetrieveAPIView(RetrieveAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class LinkUpdateAPIView(UpdateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class LinkDestroyAPIView(DestroyAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
