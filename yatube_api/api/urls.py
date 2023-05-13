from rest_framework import routers
from django.urls import include, path
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
]
