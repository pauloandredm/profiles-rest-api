from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.order_by('-created_on')[0:10]
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
       
        serializer.save(user_profile=self.request.user)

    