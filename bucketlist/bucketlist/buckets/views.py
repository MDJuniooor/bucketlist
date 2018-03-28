from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from bucketlist.users import models as user_models
from bucketlist.users import serializers as user_serializers


class ListAllBucket(APIView):

    def get(self, request, format=None):

        print(request.user)

        all_buckets = models.Bucket.objects.all()

        serializer = serializers.BucketSerializer(all_buckets, many=True, context={'request': request})

        return Response(data=serializer.data)

class LikeBucket(APIView):

    def get(self, request, bucket_id, format=None):
        
        likes = models.Like.objects.filter(bucket__id=bucket_id)

        like_creators_ids = likes.values('creator_id')

        users = user_models.User.objects.filter(id__in=like_creators_ids)

        serializer = user_serializers.ListUserSerializer(
            users, many=True, context={"request": request})
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, bucket_id, format=None):

        user = request.user
        print(user)
        try:
            found_bucket = models.Bucket.objects.get(id=bucket_id)

        except models.Bucket.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                bucket=found_bucket
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        
        except models.Like.DoesNotExist:
            
            new_like = models.Like.objects.create(
                creator=user,
                bucket=found_bucket
            )

            new_like.save()

            return Response(status=status.HTTP_201_CREATED)


class UnLikeBucket(APIView):

    def delete(self, request, bucket_id, format=None):

        user = request.user

        try:
            preexisiting_like = models.Like.objects.get(
                creator=user,
                bucket__id=bucket_id
            )
            preexisiting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)


class CommentOnBucket(APIView):

    def post(self, request, bucket_id, format=None):

        user = request.user
        
        try:
            found_bucket = models.Bucket.objects.get(id=bucket_id)
        except models.Bucket.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(creator=user, bucket=found_bucket)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Comment(APIView):

    def delete(self, request, comment_id, format=None):

        user=request.user

        try:
            comment = models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)





class BucketDetail(APIView):

    def find_own_bucket(self, bucket_id, user):
        try:
            bucket = models.Bucket.objects.get(id=bucket_id, creator=user)
            return bucket
        except models.bucket.DoesNotExist:
            return None

    def get(self, request, bucket_id, format=None):

        user = request.user

        try:
            bucket = models.Bucket.objects.get(id=bucket_id)
        except models.Bucket.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.BucketSerializer(bucket, context={'request':request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, bucket_id, format=None):

        user = request.user

        bucket = self.find_own_bucket(bucket_id, user)

        if bucket is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.InputBucketSerializer(
            bucket, data=request.data, partial=True)
        

        if serializer.is_valid():

            serializer.save(creator=user)

            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, bucket_id, format=None):

        user=request.user
        
        bucket = self.find_own_bucket(bucket_id, user)

        if bucket is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        bucket.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class Search(APIView):

    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags',None)

        if hashtags is not None:

            hashtags = hashtags.split(",")

            buckets = models.bucket.objects.filter(tags__name__in=hashtags)

            serializer = serializers.BucketSerializer(buckets, many=true)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        else:

            return Response(status=status.HTTP_204_NO_CONTENT)


class ModerateComments(APIView):

    def delete(self, request, bucket_id, comment_id, format=None):

        user = request.user

        try:
            comment_to_delete = models.Comment.objects.get(
                id=comment_id, bucket__id=bucket_id, bucket__creator=user)
            comment_to_delete.delete()
        
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
