from django.shortcuts import render

from allauth.socialaccount.models import SocialAccount

from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Google_Serializer  # Import your serializer
from django.shortcuts import get_object_or_404

# Create your views here.
class User_Data(APIView):
    def get(self,request):
        user_data = User.objects.get(username=request.user)
        serializer=User_Serializer(user_data)
        return Response(serializer.data)
    

@api_view(['GET'])
def register(request):
    user_data = User.objects.get(username=request.user)
    serializer=User_Serializer(user_data)
    return Response(serializer.data)


class SocialAccountAPIView(APIView):
    def get(self, request, *args, **kwargs):
        context = {}

        if request.user.is_authenticated:
            try:
                # Assuming you have a ForeignKey from SocialAccount to User
                google_account = get_object_or_404(
                    SocialAccount, provider='google', user=request.user)

                # Accessing user information
                user_id = google_account.uid
                email = google_account.extra_data.get('email')
                full_name = google_account.extra_data.get('name')
                profile_picture_url = google_account.extra_data.get('picture')

                context = {
                    'user_id': user_id,
                    'email': email,
                    'full_name': full_name,
                    'profile_picture_url': profile_picture_url,
                }

                # Serialize the data
                serializer = Google_Serializer(data=context)
                serializer.is_valid()
                return Response(serializer.data, status=status.HTTP_200_OK)

            except SocialAccount.DoesNotExist:
                pass

        # If the user is not authenticated or no SocialAccount exists
        return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
