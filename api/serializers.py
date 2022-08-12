from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Post, Comment, Friendship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class PostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = ['user', 'id', 'description', 'date_created', 'likes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'id', 'comment', 'date_created', 'likes']


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['user', 'friend']

