from django.contrib import admin
from django.urls import path, include
from .api import api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', api_views.RegistrationView.as_view(),),
    path('auth/', include('rest_framework_social_oauth2.urls'))

]