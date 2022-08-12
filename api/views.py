from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, generics, mixins, status
from rest_framework import permissions
from rest_framework.views import APIView

from api.models import Post, Comment, Friendship
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-date_created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class FriendshipView(mixins.DestroyModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    def post(self, request, pk=None):
        user = self.request.user
        friend = User.objects.get(pk=pk)
        friendship = Friendship.objects.create(user=user, friend=friend)
        friendship.save()
        return JsonResponse({'message': 'Friendship has been added'}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        user = self.request.user
        friend = User.objects.get(pk=pk)
        friendship = Friendship.objects.get(user=user, friend=friend)
        friendship.delete()
        return JsonResponse({'message': 'Friendship has been removed'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def like_post_view(request, pk):
    post = Post.objects.filter(pk=pk).first()
    post.likes += 1
    post.save()
    return JsonResponse({'message': 'post liked correctly'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def dislike_post_view(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if post.likes > 0:
        post.likes -= 1
        post.save()
        return JsonResponse({'message': 'post disliked correctly'}, status=status.HTTP_200_OK)
    return JsonResponse({'error': 'something went wrong'}, status=status.HTTP_400_OK)






