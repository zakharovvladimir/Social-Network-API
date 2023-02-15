"""API Serializers."""
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        """Post Serializer Meta."""

        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Group Serializer."""

    class Meta:
        """Group Serializer Meta."""

        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',

    )

    class Meta:
        """Comment Serializer Meta."""

        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer."""

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',)
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault())

    class Meta:
        """Follow Serializer Meta."""

        model = Follow
        fields = '__all__'
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message=("You've already subscribed")
            ),
        )

    def validate(self, data):
        """Follow Serializer validate func."""
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                "You're trying to subscribe yourself")
        return data
