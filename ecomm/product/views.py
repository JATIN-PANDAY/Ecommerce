from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import * 

# Create your views here.



def get_product(request,uid,slug):
    product = Product.objects.get(uid= uid)
    size_variant = SizeVariant.objects.filter(product=product)
    # Color Variant
    color_variant=ColorVariant.objects.filter(product=product)
    # print(color_variant)

    context = { 'product':product,'size_variant':size_variant,'color_variant':color_variant}
    
    # if request.GET.get('size'):
    #     size=request.GET.get('size')
    #     price=product.get_product_price_by_size(size)
    #     context['select_size']=size
    #     context['updated_price']=price
    #     print(price)
    
    if  request.GET.get('color'):
        color=request.GET.get('color')
        color_price=product.get_product_price_by_color(color)
        context['select_color']=color
        context['color_price']=color_price
        print(color_price)
    
        color_image=ColorVariant.objects.get(color_name=color)
        context['color']=color_image
        print(color_image)
    
    return render(request,'product/product.html',context=context)
    



# Fetch product image by color

def product_image(request,uid):
    # product = Product.objects.filter(uid= uid)
    color=ColorVariant.objects.get(uid=uid)
    image=ProductImage.objects.filter(color_image=color)
    context={
        'color':color,
        'image':image
    }
    print(image)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



#############################################################

# Additional Work

def get_size(request,uid,size_name):
    # if request.method=='POST':
    select_size=request.POST.get('select_size')
    product=Product.objects.get(uid=uid)
    size=SizeVariant.objects.get(size_name=select_size)
    print('size variant:',size)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
