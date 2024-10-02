from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PostModel
from django.contrib.auth import authenticate

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  

    class Meta:
        model = PostModel
        fields = ['id', 'title', 'content', 'tags', 'author', 'created_at', 'updated_at']