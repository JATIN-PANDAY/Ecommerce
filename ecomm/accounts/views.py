# from cmath import log
# from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from product.models import *
from datetime import datetime,timedelta
import regex as re
# from home import views


from django.conf import settings    
from instamojo_wrapper import Instamojo
"import pdb; pdb.set_trace()"

api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.AUTH_TOKEN,endpoint="https://test.instamojo.com/api/1.1/")  




def register_page(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(email = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
            # email regex
        email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search (email_condition,email):
            password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
            if re.match(password_pattern,password):

                user_obj = User.objects.create(email = email ,password=password ,name=name )

                messages.success(request, 'An email has been sent on your mail.')
                return HttpResponseRedirect(request.path_info)
            else:
                messages.warning(request,'Use strong password')
                return HttpResponseRedirect(request.path_info)

        else:
            messages.warning(request, 'Invalid email.')
            return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')



def activate_email(request,email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Your email verified.')
        return redirect('/account/login')
    
    except Exception as e:
        return HttpResponse('Invalid Email token')




def login_page(request):

    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
        
            user_obj = User.objects.get(email = email)
            
            profile=Profile.objects.filter(user=user_obj)

            if user_obj:
                if user_obj.profile.is_email_verified:
                    if user_obj.password==password:
                        
                        response= redirect('/')
                        response.set_cookie('email',email,expires=datetime.utcnow()+timedelta(days=1))
                        response.set_cookie('password',password,expires=datetime.utcnow()+timedelta(days=1))
                        response.set_cookie('uid',user_obj.uid,expires=datetime.utcnow()+timedelta(days=1))
                        response.set_cookie('name',user_obj.name,expires=datetime.utcnow()+timedelta(days=1))
                        
                        return response
        
                        
                    else:
                        messages.warning(request, 'Incorrect Password')
                        return HttpResponseRedirect(request.path_info)
                else:
                    messages.warning(request, 'Your email is not verify')
                    return HttpResponseRedirect(request.path_info)
            else:
                messages.warning(request, 'Invalid credentials')
                return HttpResponseRedirect(request.path_info)
    except Exception as e:
        messages.warning(request,'Incorrecr Email')
        return HttpResponseRedirect(request.path_info)

    return render(request ,'accounts/login.html')


# Logout

def logout(request):
    response= redirect('/')
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('uid')
    response.delete_cookie('password')
    return response

# Adding add to cart functionality

def add_to_Cart(request,uid):
    if 'uid' in request.COOKIES and 'email' in request.COOKIES:
        
        variant=request.GET.get('color')

        if request.method=='POST':
            user = request.COOKIES['uid']
            profile = Profile.objects.get(user=user)
            product = Product.objects.get(uid=uid)
                
            size=request.POST.get('select_size')
            
            if variant :
                variant=request.GET.get('color')
                color_variant=ColorVariant.objects.get(color_name=variant)


                if size :
                    # variant=request.GET.get('color')
                    size_variant=SizeVariant.objects.get(uid=size)
                    cart , _ = Cart.objects.get_or_create(user=profile,is_paid=False)
                    cartitems = CartItems.objects.create(cart=cart,product=product,size_variant=size_variant,color_variant=color_variant)
                    messages.success(request, 'Item added successfully.')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                else:
                    messages.warning(request, 'Please select size.')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.warning(request, 'Please select color.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))            
    else:
        return redirect('/account/login')


    
   
def show_cart(request):
    try:
        user = request.COOKIES['uid']
        profile = Profile.objects.get(user=user)
        cart=Cart.objects.get(user=profile,is_paid=False)
        a=cart.get_cart_total()
        print('total',a)
        if cart.get_cart_total()!=0:
        
        
            context = {
                        'cart':cart,
                        # 'a':a
                        
                    }
            return render(request,'accounts/cart.html',context)
        else:
            msg='Your Cart is Empty.'
            return render(request,'accounts/cart.html',{'msg':msg})
            
    except Exception as e:
            msg='Your Cart is Empty.'
            return render(request,'accounts/cart.html',{'msg':msg})


def cart_delete(request,uid):
    try:
        user =request.COOKIES['uid']
        profile=Profile.objects.get(user=user)
        cartitem=CartItems.objects.get(uid=uid)
        cartitem.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
    
    except Exception as e:
        print(e)



def add_to_wishlist(request,uid):
    if 'uid' in request.COOKIES and 'email' in request.COOKIES:

        user=request.COOKIES['uid']
        profile=Profile.objects.get(user=user)
        product=Product.objects.get(uid=uid)
        wishlist , _ =Wishlist.objects.get_or_create(user=profile)

        wishlist_item=WishlistItems.objects.create(wishlist=wishlist,product=product)
        
        messages.success(request,'Item added in wishlist')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/account/login')

def get_wishlist(request):
    user=request.COOKIES['uid']
    try:
        profile=Profile.objects.get(user=user)
        # product=Product.objects.get(uid=uid)
        wishlist=Wishlist.objects.get(user=profile)
        # wishlistitems=WishlistItems.objects.filter(wishlist=wishlist)
        
        total_items=wishlist.wishlistitems.count()
        print('Items',total_items)
        if total_items!=0:
            context={
                # 'product':product,
                'wishlist':wishlist,
                'total_items':total_items
            }
            return render(request,'accounts/wishlist.html',context)
        else:
            msg='No items in wishlist'
            return render(request,'accounts/wishlist.html',{'msg':msg})
    except Exception as e:
            msg='No items in wishlist'
            return render(request,'accounts/wishlist.html',{'msg':msg})

        
    
def wishlist_item_delete(request,uid):
    try:
        user=request.COOKIES['uid']
        profile=Profile.objects.get(user=user)
        wishlist=WishlistItems.objects.get(uid=uid)
        wishlist.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def order_process(request,uid):
    if 'uid' in request.COOKIES and 'email' in request.COOKIES:
        
        variant=request.GET.get('color')
        
        user=request.COOKIES['uid']
        profile=Profile.objects.get(user=user)
        product=Product.objects.get(uid=uid)

        if variant:
            color_variant=ColorVariant.objects.get(color_name=variant)
            size_variant=SizeVariant.objects.filter(product=product)

            color_price=product.get_product_price_by_color(color_variant)


            context={
                'product':product,
                'color_variant':color_variant,
                'size_variant':size_variant,
                'color_price':color_price
            }
            return render(request,'accounts/orderpage.html',context)
        else:
            messages.warning(request,'select color.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/account/login')

def order_submit(request,uid):
    if request.method=='POST':
        user=request.COOKIES['uid']
        email=request.COOKIES['email']
        name=request.COOKIES['name']


        profile = Profile.objects.get(user=user)
        product = Product.objects.get(uid=uid)
        color=request.POST.get('color_variant')    
        size=request.POST.get('select_size')
        price=request.POST.get('price')
        
        color_variant=ColorVariant.objects.get(color_name=color)
        color_price=product.get_product_price_by_color(color_variant)

        if size:
            size_variant=SizeVariant.objects.get(uid=size)
            print('Size_variant:',size_variant)

            order=Order.objects.create(user=profile,product=product,size_variant=size_variant,color_variant=color_variant,price=price)

            response = api.payment_request_create(
            amount=color_price,  
            purpose = 'Order',
            buyer_name = name,
            email=email ,              
            redirect_url = "http://127.0.0.1:8000/account/order_success_page",
            
        )

            print(response)
            order.order_id=response['payment_request']['id']
            order.save()


            # order=Order.objects.create(user=profile,product=product,color_variant=color_variant)
            context={
                'user':user,
                'product':product,
                'color_variant':color_variant,
                'size_variant':size_variant,
                'color_price':color_price,
                'payment_url':response['payment_request']['longurl']

            }
            return render(request,'accounts/payment.html',context)

            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        else:
            messages.warning(request,'Select size')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('Hii')


def payment_process(request,uid):
    user=request.COOKIES['uid']
    profile=Profile.objects.get(user=user)



def order_success_page(request):
    user=request.COOKIES['uid']
    profile = Profile.objects.get(user=user)
    payment_request=request.GET.get('payment_request_id')
    order=Order.objects.get( order_id=payment_request )
    order.is_paid=True
    order.save()
    return render(request,'accounts/order_success.html')
   
def profilepage(request,uid):
    uid=request.COOKIES['uid']
    # email=request.COOKIES['email']
    # name=request.COOKIES['name']
    user=User.objects.get(uid=uid)

    profile = Profile.objects.get(user=user)
    context={'user':user,
    'profile':profile,
    # 'name':name,
    # 'email':email
    }
    return render(request,'accounts/profile.html',context)

def updateprofile(request):
    uid=request.COOKIES['uid']
    # email=request.COOKIES['email']
    # name=request.COOKIES['name']
    user=User.objects.get(uid=uid)
    a=user.email
   
    profile = Profile.objects.get(user=user)

    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('contact')
        state=request.POST.get('state')
        city=request.POST.get('city')
        pin=request.POST.get('pincode')
        address=request.POST.get('address')
        email=request.POST.get('email')
        
        user.name=name
        user.email=email
        profile.contact=phone
        profile.state=state
        profile.city=city
        profile.pincode=pin
        profile.address=address
        profile.save()
        user.save()
        messages.success(request,'Profile Updated.')
        url=f'/account/profilepage/{uid}'
        return redirect(url)



   
def orderpage(request):
    try:
        uid = request.COOKIES['uid']
        user=User.objects.get(uid=uid)
        profile = Profile.objects.get(user=user)
        order=Order.objects.filter(user=profile,is_paid=True)
        context={
            'user':user,
            'profile':profile,
            'order':order

        }
        return render(request,'accounts/userorderpage.html',context)
    except Exception as e:
        msg='No orders'
        context={
            'msg':msg
            }
        return render(request,'accounts/userorderpage.html',context)
