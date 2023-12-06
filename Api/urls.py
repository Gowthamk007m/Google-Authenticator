from django.urls import path
from .views import *
urlpatterns = [
    path('User/', User_Data.as_view(), name='user_data'),
    path('social-account/', SocialAccountAPIView.as_view(),
         name='social_account_api'),


]
