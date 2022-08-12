from rest_framework import routers
from api import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'comments', views.CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostViewSet.as_view, name='posts'),
    path('friendship/add-friend/<int:pk>/', views.FriendshipView.as_view(), name='friendship'),
    path('posts/<int:pk>/like/', views.like_post_view, name='like'),
    path('posts/<int:pk>/dislike/', views.dislike_post_view, name='dislike'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]