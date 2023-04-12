from rest_framework import serializers
from .models import Post
from rest_framework.response import Response
from rest_framework import status   


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Post
        fields = ['title', 'blog']
    
    def create(self, validated_data):
        author = self.context
        print(author['user'], "Blog owner")
        post_data = Post.objects.create(author = author['user'],**validated_data)
        return post_data   

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UpdateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['author']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.blog = validated_data.get('blog', instance.blog)
        instance.save()
        return instance