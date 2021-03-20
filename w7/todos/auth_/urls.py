from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

urlpatterns = [
    path(r'login/', obtain_jwt_token)
]