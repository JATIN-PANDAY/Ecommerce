from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse

from product.models import *
from accounts.models import * 

# Create your views here.

def index(request):
    try:
        if 'uid' in request.COOKIES and 'email' in request.COOKIES:
            email=request.COOKIES['email']
            uid=request.COOKIES['uid']
            name=request.COOKIES['name']
            password=request.COOKIES['password']


            user = User.objects.get(uid=uid)
            profile = Profile.objects.get(user=user)
            product = Product.objects.all()
        
            cart = CartItems.objects.filter(cart__is_paid=False,cart__user=profile).count()
            wishlist=WishlistItems.objects.filter(wishlist__user=profile).count()

            context = {
            'user':user,
            'product':product,
            'cart':cart,
            'wishlist':wishlist,
            'email':email,
            'uid':uid,
            'name':name,
            'password':password
            
            }
            return render(request,'app/index.html',context)
        else:
            product=Product.objects.all()
            return render(request,'app/index.html',{'product':product})
    except Exception as e:
        product=Product.objects.all()
        return render(request,'app/index.html',{'product':product})


def search_item(request):
    try:
    
        if request.method=='POST':
            search=request.POST.get('search')
            product=Product.objects.filter(product_name__icontains=search)
            if product:
                return render(request,'app/search.html',{'product':product})


            else:
                product=Product.objects.all()
                return render(request,'app/search.html',{'product':product})
    
    except Exception as e:
        print(e)
    
    # return render(request,'app/search.html',{'product':product})


def price_filter(request):
    price = request.POST.get('price')
    product=Product.objects.filter(price=price)
    if product:
        return render(request,'app/index.html',{'product':product})
    else:
        messages.error(request,'No item in this price')
        return render(request,'app/index.html')

