from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserProfileFeedViewSet(viewsets.ModelViewSet):

# .filter(models.UserProfile.email == models.ProfileFeedItem.user_profile)

# if User.objects.filter(username=username).exists():

#   user = User.objects.get(username=username)
# 	posts = user.posts.all()
# 	context = {'user':user, 'posts':posts}
# 	return render(request, 'twitter/profile.html', context)

# def ListListView(request):
#     current_user = request.user
#     user_list = simpleList.objects.filter(author=current_user)
#     return render(render, 'templates/list_list.html', {'userlist': user_list})
    
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.order_by('-created_on')[0:10]
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
    
    def get_queryset(self):
        return models.ProfileFeedItem.objects.exclude(user_profile = self.request.user).order_by('-created_on')[0:10]
    
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

    