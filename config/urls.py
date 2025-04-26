from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework.routers import DefaultRouter

from core.authentication.views import CustomTokenObtainPairView, UserViewSetList

router = DefaultRouter()
router.register(r'users', UserViewSetList, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
