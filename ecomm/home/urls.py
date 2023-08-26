from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
     path('', views.index,name='index'),
     path('search_item',views.search_item,name='search_item'),
     path('price_filter',views.price_filter,name='price_filter'),
]
