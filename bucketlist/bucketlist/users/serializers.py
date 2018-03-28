from rest_framework import serializers
from . import models
from bucketlist.buckets import serializers as buckets_serializers

class UserProfileSerializer(serializers.ModelSerializer):

    buckets = buckets_serializers.CountBucketSerializer(many=True, read_only=True)
    post_count = serializers.ReadOnlyField()

class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
            'following'
        )
        

class SignUpUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'password'
        )

class DonateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'donation',
        )