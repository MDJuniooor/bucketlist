from rest_framework import serializers
from . import models
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from bucketlist.users import models as user_models

class SmallBucketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bucket
        fields = (
            'file',
        )

class CountBucketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bucket
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count'
        )

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'name',
        )

class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = (
            'creator',
        )

class InputBucketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bucket
        fields = (
            'file',
            'location',
            'caption',
        )


class BucketSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = models.Bucket
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator',
            'tags',
            'natural_time',
            'is_liked'
        )

    def get_is_liked(self, obj):
        if 'request' in self.context:
            request = self.context['request']
            try:
                models.Like.objects.get(creator__id=request.user.id, bucket__id=obj.id)
                return True
            except models.Like.DoesNotExist:
                return False
        return False
