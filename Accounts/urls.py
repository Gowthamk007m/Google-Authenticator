from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    # path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),


    path('profile/', views.profile_view, name='profile_view'),

    




]
