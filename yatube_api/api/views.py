"""API views."""
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import UserPermission
from .serializers import (CommentSerializer,
                          GroupSerializer,
                          PostSerializer,
                          FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """GET, POST, PUT, PATCH, DELETE."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (UserPermission,
                          permissions.IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Post modification."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """GET."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """GET, POST, PUT, PATCH, DELETE."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (UserPermission,
                          permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Comment modification."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        """Comment request."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    """Follow API."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Follow request."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Follow modification."""
        serializer.save(user=self.request.user)
