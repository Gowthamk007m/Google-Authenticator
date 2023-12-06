from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home_page'),
    path('products', views.Shop_page, name='shop_page'),

]
