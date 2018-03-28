from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class ExploreUsers(APIView):

    def get(self, request, format=None):

        last_five = models.User.objects.all().order_by('-date_joined')[:5]

        serializer = serializers.ListUserSerializer(
            last_five, many=True, context={"request": request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class SignUpUser(APIView):

    def post(self, request, format=None):

        serializer = serializers.SignUpUserSerializer(data=request.data)

        if serializer.is_valid():
            
            serializer.save()
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):

    def delete(self, request, username, format=None):

        try:
            found_User = models.User.objects.get(username=username)
            found_User.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.User.DoesNotExist:   
            return Response(status=status.HTTP_404_NOT_FOUND)

        except Exception as e: 
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonateUser(APIView):

    def put(self, request, username, format=None):

        try:
            found_User = models.User.objects.get(username=username)
            donation = models.User.objects.get(username=username).donation
            
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        serializer = serializers.DonateUserSerializer(found_User, data=request.data,)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
