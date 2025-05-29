from django.urls import path

from main.apps import MainConfig
from main.views import (
    AgentCreateAPIView,
    AgentListAPIView,
    AgentRetrieveAPIView,
    AgentUpdateAPIView,
    AgentDestroyAPIView,
    ProductCreateAPIView,
    ProductListAPIView,
    ProductRetrieveAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    LinkCreateAPIView,
    LinkListAPIView,
    LinkRetrieveAPIView,
    LinkUpdateAPIView,
    LinkDestroyAPIView,
)

app_name = MainConfig.name


urlpatterns = [
    path("agent/create/", AgentCreateAPIView.as_view(), name="agent-create"),
    path("agent/list/", AgentListAPIView.as_view(), name="agent-list"),
    path("agent/<int:pk>/detail", AgentRetrieveAPIView.as_view(), name="agent-detail"),
    path("agent/<int:pk>/update", AgentUpdateAPIView.as_view(), name="agent-update"),
    path("agent/<int:pk>/delete", AgentDestroyAPIView.as_view(), name="agent-destroy"),
    path("product/create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("product/list/", ProductListAPIView.as_view(), name="product-list"),
    path(
        "product/<int:pk>/detail",
        ProductRetrieveAPIView.as_view(),
        name="product-detail",
    ),
    path(
        "product/<int:pk>/update", ProductUpdateAPIView.as_view(), name="product-update"
    ),
    path(
        "product/<int:pk>/delete",
        ProductDestroyAPIView.as_view(),
        name="product-destroy",
    ),
    path("link/create/", LinkCreateAPIView.as_view(), name="link-create"),
    path("link/list/", LinkListAPIView.as_view(), name="link-list"),
    path("link/<int:pk>/detail", LinkRetrieveAPIView.as_view(), name="link-detail"),
    path("link/<int:pk>/update", LinkUpdateAPIView.as_view(), name="link-update"),
    path("link/<int:pk>/delete", LinkDestroyAPIView.as_view(), name="link-destroy"),
]
