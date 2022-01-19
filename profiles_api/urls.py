from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

router = DefaultRouter()
router.register('feed', views.UserProfileFeedViewSet)
router.register('register', views.UserProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]