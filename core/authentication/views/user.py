from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from core.authentication.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserUpdateSerializer

from core.authentication.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from core.authentication.serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserViewSetList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        return UserSerializer

    http_method_names = ['get', 'post', 'patch', 'put']

    ordering_fields = ['id']
    ordering = ['id']
