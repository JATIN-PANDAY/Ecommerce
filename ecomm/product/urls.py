from django.contrib import admin
from django.urls import path
from product import views


urlpatterns = [
     path('<uid>/<slug>',views.get_product,name='get_product'),

     # path('<uid>/<slug>/',views.get_product,name='get_product'),
     path('product_image/<uid>',views.product_image,name='product_image'),
     path('get_size/<uid>/<size_name>',views.get_size,name='get_size'),
     # path('color',views.color,name='color'),
]
