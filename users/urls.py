from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UsersList, UsersDetail

app_name = UsersConfig.name

urlpatterns = [
    path("list/", UsersList.as_view(), name="users-list"),
    path("<int:pk>/", UsersDetail.as_view(), name="users-detail"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
