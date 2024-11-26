from django.urls import path

from users.apps import UsersConfig
from users.views import UsersList, UsersDetail

app_name = UsersConfig.name

urlpatterns = [
    path('list/', UsersList.as_view(), name="users-list"),
    path('<int:pk>/', UsersDetail.as_view(), name="users-detail"),
]
