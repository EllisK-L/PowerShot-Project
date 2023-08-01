"""PowerShotProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import RegisterAPIView, CommentListAPIView, CommentCreateAPIView, FollowAPIView
from api.views import UserViewSet, UploadsCreateView, UploadsListView, likeAPIView, UserListView

router = DefaultRouter()
router.register(r'user',UserViewSet, basename="user")

# router.register(r'upload', UploadsViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path("register", RegisterAPIView.as_view()),
    path('upload/', UploadsCreateView.as_view()),
    path('uploads/',UploadsListView.as_view()),
    path('like/', likeAPIView.as_view()),
    path('comments/',CommentListAPIView.as_view()),
    path('create_comment/',CommentCreateAPIView.as_view()),
    path('follow/',FollowAPIView.as_view()),
    path('users/', UserListView.as_view())
]