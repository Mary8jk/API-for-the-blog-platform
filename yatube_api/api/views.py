from rest_framework import viewsets
from http import HTTPStatus
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from posts.models import Post, User, Group, Comment, Follow
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .serializers import (UserSerializer, PostSerializer,
                          GroupSerializer, CommentSerializer,
                          FollowSerializer)
from .permission import IsOwner, IsReadOnly
from rest_framework import mixins
from rest_framework.filters import SearchFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwner, IsReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request):
        return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwner, IsReadOnly)

    def get_queryset(self, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        return super().get_queryset().filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=self.request.user,
            post=post
        )


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
