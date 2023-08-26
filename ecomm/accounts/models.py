
from django.db import models
# from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email
from product.models import *



class User(BaseModel):
    
    name=models.CharField(max_length=50,blank=True)    
    email=models.CharField(max_length=100,blank=True)
    password=models.CharField(max_length=100,blank=True)
# 
class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    state = models.CharField(max_length=100 , null=True , blank=True)
    city = models.CharField(max_length=100 , null=True , blank=True)
    address = models.CharField(max_length=100 , null=True , blank=True)
    contact = models.IntegerField( null=True , blank=True)
    pincode =  models.IntegerField( null=True , blank=True)

    
    # profile_image = models.ImageField(upload_to = 'profile')

    def __str__(self):
        return self.user.name

    
class Cart(BaseModel):
    user = models.ForeignKey('Profile', related_name='profile', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    # instamojo_id=models.CharField(max_length=500)

    def get_cart_total(self):
        cart_items=self.cartitems.all()
        price=[]
        for cart_item in cart_items:
            price.append(cart_item.product.price)
            if cart_item.color_variant:
                color_variant_price=cart_item.color_variant.price
                price.append(color_variant_price)
        print(price)
        return sum(price)



    

class CartItems(BaseModel):
    cart =  models.ForeignKey(Cart,related_name='cartitems', on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='product',on_delete=models.SET_NULL,null=True,blank=True)
    size_variant = models.ForeignKey(SizeVariant,related_name='size_variant',on_delete=models.CASCADE,null=True,blank=True)
    color_variant = models.ForeignKey(ColorVariant,related_name='color_variant',on_delete=models.CASCADE,null=True,blank=True)

    def get_product_price(self):
        price=[self.product.price]

        # if self.size_variant:
        #     size_variant_price=self.size_variant.price
        #     price.append(size_variant_price)
        if self.color_variant:
            color_variant_price=self.color_variant.price
            price.append(color_variant_price)
        return sum(price)

class Wishlist(BaseModel):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
  
class WishlistItems(BaseModel):
    wishlist =  models.ForeignKey(Wishlist, related_name='wishlistitems',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
class Order(BaseModel):
    user = models.ForeignKey('Profile',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    size_variant = models.ForeignKey(SizeVariant,on_delete=models.CASCADE,null=True,blank=True)
    color_variant = models.ForeignKey(ColorVariant,on_delete=models.CASCADE,null=True,blank=True)
    price=models.IntegerField()
    is_paid = models.BooleanField(default=False)
    order_id=models.TextField(null=True)


@receiver(post_save , sender = User)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)
