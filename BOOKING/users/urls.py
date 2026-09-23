from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


app_name = 'users'


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', views.UserProfileView.as_view(), name='profile'),
    path('change-profile/', views.UserChangeProfileView.as_view(), name='change_profile'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]





