from django.contrib import admin
from django.urls import path,include
from accounts import views


urlpatterns = [
    #  path('', views.index,name='index'),

     path('register/', views.register_page,name='register'),
     path('login/', views.login_page,name='login'),
     path('logout',views.logout,name='logout'),
     path('activate/<email_token>',views.activate_email,name='activate'),
     path('add_to_Cart/<uid>',views.add_to_Cart,name='add_to_Cart'),
     path('cart',views.show_cart,name='cart'),
     path('cart_delete/<uid>',views.cart_delete,name='cart_delete'),
     path('add_to_wishlist/<uid>',views.add_to_wishlist,name='add_to_wishlist'),
     path('get_wishlist',views.get_wishlist,name='get_wishlist'),
     path('wishlist_item_delete/<uid>',views.wishlist_item_delete,name='wishlist_item_delete'),
     path('order_process/<uid>',views.order_process,name='order_process'),
     path('order_submit/<uid>',views.order_submit,name='order_submit'),
     path('payment_process/<uid>',views.payment_process,name='payment_process'),
     path('order_success_page',views.order_success_page,name='order_success_page'),
     path('profilepage/<uid>',views.profilepage,name='profilepage'),
     path('updateprofile',views.updateprofile,name='updateprofile'),
     path('orderpage',views.orderpage,name='orderpage'),

]