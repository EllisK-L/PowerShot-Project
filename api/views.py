from django.shortcuts import render
from rest_framework import generics
from api.serializers import RegisterSerializer, UserSerializer, UploadsSerializer, UploadsListSerializer, CommentSerializer
from api.models import PSPUser, Comment
from api.models import Uploads
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.


class RegisterAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        queryset = Token.objects.all()
        user = get_object_or_404(queryset, key=pk).user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UploadsCreateView(generics.CreateAPIView):
    queryset = Uploads.objects.all()
    serializer_class = UploadsSerializer

class UploadsListView(generics.ListAPIView):
    serializer_class = UploadsListSerializer

    def get_queryset(self):
        user_queryset = PSPUser.objects.all()
        username = self.request.GET.get("username")
        if username:
            user = get_object_or_404(user_queryset, username=username)
            queryset = Uploads.objects.filter(user = user).order_by("-date")
        else:
            queryset = Uploads.objects.all().order_by("-date")
        return queryset

class likeAPIView(APIView):

    def post(self, request, format=None):
        # params token, username, post_id
        token = request.data.get("token")
        post_id = request.data.get("post_id")

        message = ""

        token_queryset = Token.objects.all()
        user = get_object_or_404(token_queryset, key=token).user
        upload = Uploads.objects.get(id=post_id)
        print(upload.likes.all())
        if not upload.likes.filter(pk=user.id).exists():
            message = "liked"
            upload.likes.add(user)
        else:
            message = "unliked"
            upload.likes.remove(user)
        return Response({"msg":message})
    
class FollowAPIView(APIView):

    def post(self, request, format=None):
        token = request.data.get("token")
        follow_username = request.data.get("follow_username")

        message = ""

        token_queryset = Token.objects.all()
        user = get_object_or_404(token_queryset, key=token).user
        follow_user_queryset = PSPUser.objects.all()
        follow_user = get_object_or_404(follow_user_queryset,username=follow_username)
        if not user.following.filter(pk=follow_user.id).exists():
            message = "followed"
            user.following.add(follow_user)
        else:
            message = "unfollowed"
            user.following.remove(follow_user)
        return Response({"msg":message})
    

class CommentListAPIView(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        upload_id = self.request.GET.get("upload_id")
        upload = Uploads.objects.get(id=upload_id)
        comments = Comment.objects.filter(upload=upload).order_by("-date")
        return comments
    
class CommentCreateAPIView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

class UserListView(generics.ListAPIView):
    queryset = PSPUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']