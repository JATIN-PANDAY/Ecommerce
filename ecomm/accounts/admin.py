from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Wishlist)
admin.site.register(WishlistItems)
admin.site.register(Order)