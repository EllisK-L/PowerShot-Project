from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import PSPUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from .models import Uploads, Comment

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSPUser
        fields = ["username"]

class UserSerializer(serializers.ModelSerializer):
    following = FollowingSerializer(many=True)
    class Meta:
        model = PSPUser
        fields = ["first_name","last_name","username","email", "bio", "following"]

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=PSPUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = PSPUser
        fields = ['username','password','password2','email','first_name','last_name']

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        return attrs
    
    def create(self, validation_data):
        user = PSPUser.objects.create(
            username=validation_data["username"],
            email=validation_data["email"],
            first_name=validation_data["first_name"],
            last_name=validation_data["last_name"]
        )

        user.set_password(validation_data["password"])
        user.save()
        return user
    

class UploadsSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, write_only=True)
    caption = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
    
    class Meta:
        # list_serializer_class = UploadsListSerializer
        model = Uploads
        fields = ['caption', 'description', 'image', "token"]
    
    def create(self, validation_data):
        upload = Uploads.objects.create(
            user = Token.objects.get(key=validation_data["token"]).user,
            caption = validation_data["caption"],
            description = validation_data["description"],
            image = validation_data["image"]
        )
        upload.save()
        return upload 

class UploadsListSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True)
    username = serializers.CharField(write_only=True)
    user=UserSerializer()
    class Meta:
        model = Uploads
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    commenter = UserSerializer(required=False)
    upload = serializers.CharField(required=False)
    upload_id = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validation_data):
        comment = Comment.objects.create(
            upload_id=validation_data["upload_id"],
            commenter=Token.objects.get(key=validation_data["token"]).user,
            text=validation_data["text"],   
        )
        comment.save()
        return comment

# class FollowSerializer(serializers.ModelSerializer):

